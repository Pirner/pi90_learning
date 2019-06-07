"""Class definition for Djikstra algorithm node."""
# !/usr/bin/env python
# -*- coding: utf-8 -*- #

import numpy as np


class AdalineGD(object):
    """Perceptron class."""

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        """Initialize the perceptron."""
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, x, y):
        """Method to train the perceptron."""
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + x.shape[1])

        self.errors_ = []
        self.cost_ = []

        for i in range(self.n_iter):
            net_input = self.net_input(x)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * x.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)

        return self

    def net_input(self, x):
        """Nettoeingabe berrechnen."""
        return np.dot(x, self.w_[1:]) + self.w_[0]

    def activation(self, x):
        """Lineare Aktivierungsfunktion berechnen."""
        return x

    def predict(self, x):
        """Klassenbezeichnung zurueckgeben."""
        return np.where(self.net_input(x) >= 0.0, 1, -1)
