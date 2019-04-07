"""This module queries creates a bayes spam filter."""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import mysql.connector

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


print('number of spam mails in corpus: {}'.format(n_spam))
print('numer of ham mails in corpus: {}'.format(n_ham))
