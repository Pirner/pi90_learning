"""This module queries creates a bayes spam filter."""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mysql.connector
from math import log as math_log

from .utils import content_as_vector


class BayesSpamfilter():
    """Class which manages spam filtering based on bayes."""

    n_spam = 0
    n_ham = 0
    n_mails = 0
    pr_spam = 0
    pr_ham = 0

    probability_table = []

    def compute_pr_spammy_word(self, token, occ_spam, occ_ham):
        """Compute how spammy or hammy a word is."""
        pr_spam = occ_spam / self.n_spam
        pr_ham = occ_ham / self.n_ham

        return (pr_spam, pr_ham)

    def compute_probabilies_of_table(self):
        """Compute new probabilites according to the tables stored."""
        acc = []
        for entry in self.probability_table:
            probabilities = self.compute_pr_spammy_word(
                entry[0],
                entry[1],
                entry[2]
            )

            new_entry = [entry[0], entry[1], entry[2], probabilities[0], probabilities[1]]
            acc.append(new_entry)
        self.probability_table = acc

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

        from pudb import set_trace
        set_trace()
        self.compute_probabilies_of_table()

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

    def search_n_occurence_in_table(self, token):
        """Search for occurence of a word and return occurence as tuple."""
        ret_val = 0
        for entry in self.probability_table:
            if entry[0] == token:
                ret_val = (entry[1], entry[2])
        return ret_val

    # computes the probability of a token according to the table entry
    # obsolote method
    def compute_email_probability(self, content):
        """Compute the probability for an email to be spam."""
        # probability of the word vector
        pr_vec = math_log(self.pr_spam / self.pr_ham)

        # iterate through each word
        acc = 0.0
        for word in content_as_vector(content):
            occurence = self.search_n_occurence_in_table(word)
            pr_word_spam = 1
            pr_word_ham = 1

            if occurence[0] > 0:
                pr_word_spam = (occurence[0] / self.n_mails) / self.pr_spam
            if occurence[1] > 0:
                pr_word_ham = (occurence[1] / self.n_mails) / self.pr_ham
            acc += math_log(pr_word_spam / pr_word_ham)

        pr_vec += acc
        print(pr_vec)
