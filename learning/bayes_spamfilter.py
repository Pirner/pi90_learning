"""This module queries creates a bayes spam filter."""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mysql.connector

from .utils import content_as_vector


class BayesSpamfilter():
    """Class which manages spam filtering based on bayes."""

    n_spam = 0
    n_ham = 0
    n_mails = 0
    pr_spam = 0
    pr_ham = 0

    probability_table = []

    def __init__(self):
        """Init method."""
        print('Bayesian Spamfilter created.')

        # Initialize the probabilites from the corpus

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="admin",
            database="pi90_learning"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT content, spam FROM emails")

        emails = mycursor.fetchall()

        n_spam = 0
        n_ham = 0

        for email in emails:

            # count number of spam and ham mails
            if email[1]:
                n_spam += 1
            else:
                n_ham += 1

            self.n_spam = n_spam
            self.n_ham = n_ham

            # split content into words and transform to lowercase

            # email_content = email[0].lower().translate(
            #     str.maketrans('', '', string.punctuation)
            # ).split()
            email_content = content_as_vector(email[0])

            # create table for the tokens and their occurence
            for token in set(email_content):
                self.insert_token(token, email[1])

            # compute pr_spam and pr_ham
            self.pr_spam = (n_spam) / (n_spam + n_ham)
            self.pr_ham = (n_ham) / (n_spam + n_ham)
            self.n_mails = n_spam + n_ham

    def insert_token(self, token, spam):
        """Insert a token into the table."""
        inserted = False
        for entry in self.probability_table:
            # check if the token is already in the table
            if entry[0] == token:
                if spam:
                    entry[1] += 1
                else:
                    entry[2] += 1

                inserted = True
                break

        if inserted:
            return

        if spam:
            self.probability_table.append([token, 1, 0])
        else:
            self.probability_table.append([token, 0, 1])

    def compute_spam_probability(self, content):
        """Compute the probability for an email to be spam."""
        # probability of the word vector
        pr_vec = 1

        # iterate through each word
        for word in content_as_vector(content):
            pass

    def compute_ham_probability(self, content):
        """Compute the probability for an email to be ham."""
        pass
