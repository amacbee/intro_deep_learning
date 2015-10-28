# -*- coding: utf-8 -*-

import numpy as np


class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.hidden_weight = 0.1 * (np.random.random_sample((hidden_size, input_size+1)) - 0.5)
        self.output_weight = 0.1 * (np.random.random_sample((output_size, hidden_size+1)) - 0.5)


    def fit(self, x, t, learning_ratio=0.1):
        z, y = self.fire(x)
        dy = (y - t) * y * (1 - y)
        dz = (self.output_weight.T.dot(dy))[1:] * z * (1 - z)

        hidden_input = np.r_[np.array([1]), x]
        self.hidden_weight -= learning_ratio * dz.reshape(-1, 1) * hidden_input

        output_input = np.r_[np.array([1]), z]
        self.output_weight -= learning_ratio * dy.reshape(-1, 1) * output_input


    def fire(self, x):
        sigmoid = lambda x: 1. / (1. + np.exp(-x))

        z = np.vectorize(sigmoid)(self.hidden_weight.dot(np.r_[np.array([1]), x]))
        y = np.vectorize(sigmoid)(self.output_weight.dot(np.r_[np.array([1]), z]))

        return (z, y)


    def predicate(self, x):
        z, y = self.fire(x)
        return np.array(y).argmax()


    def save(self, fpath):
        np.savez(fpath, hidden=self.hidden_weight, output=self.output_weight)


    def load(self, fpath):
        model = np.load(fpath)
        self.hidden_weight = model['hidden']
        self.output_weight = model['output']