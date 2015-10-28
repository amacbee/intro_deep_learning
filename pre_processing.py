# -*- coding: utf-8 -*-

from sklearn.datasets import fetch_mldata
import gzip
import numpy as np
import pickle


def prepare_mnist_data():
    """
    MNIST dataset をダウンロードする処理
    :param train_N: 学習用データの個数 (残りをテスト用とする)
    :return:
    """

    with gzip.open('./data/mnist.pkl.gz', 'rb') as f:
        train, valid, test = pickle.load(f)

    np.savez('./data/mnist', X_train=train[0], X_test=test[0], y_train=train[1], y_test=test[1])


if __name__ == "__main__":
    prepare_mnist_data()
