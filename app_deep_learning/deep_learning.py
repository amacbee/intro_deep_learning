# -*- coding: utf-8 -*-

from chainer import cuda, Variable, FunctionSet, optimizers
import chainer.functions as F
import numpy as np
import pickle


class DeepLearning:
    def __init__(self, input_size, hidden_size, output_size):
        self.model = FunctionSet(l1=F.Linear(input_size, hidden_size),
                    l2=F.Linear(hidden_size, hidden_size),
                    l3=F.Linear(hidden_size, output_size))
        self.optimizer = optimizers.Adam()
        self.optimizer.setup(self.model.collect_parameters())



    def batch(self, X_train, y_train, batch_size, perm):
        train_size = X_train.shape[0]

        for i in xrange(0, train_size, batch_size):
            X_batch = X_train[perm[i: i+batch_size]]
            y_batch = y_train[perm[i: i+batch_size]]

            # Chainer用に型変換
            x = Variable(X_batch)
            t = Variable(y_batch)

            self.optimizer.zero_grads()
            y = self.forward(x)  # 予測結果

            loss = F.softmax_cross_entropy(y, t)
            loss.backward()

            self.optimizer.update()


    def forward(self, x, train=True):
        h1 = F.dropout(F.sigmoid(self.model.l1(x)),  train=train)
        h2 = F.dropout(F.sigmoid(self.model.l2(h1)), train=train)
        return self.model.l3(h2)


    def predicate(self, x_data):
        x = np.array([x_data], dtype=np.float32)
        x = Variable(x)
        y = self.forward(x, train=False)
        return np.argmax(y.data)


    def save(self, fpath):
        pickle.dump(self.model, open(fpath, 'wb'), -1)


    def load(self, fpath):
        self.model = pickle.load(open(fpath,'rb'))
