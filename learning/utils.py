"""This module provides several utility functions."""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import string


def content_as_vector(content):
    """Return content as vector."""
    # represent the content as a vector
    l_content = content.lower().translate(str.maketrans(
        '',
        '',
        string.punctuation)
    ).split()
    return l_content
