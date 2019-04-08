"""Module to read a file in subdirectory."""
import os

script_dir = os.path.dirname(__file__)
rel_path = "ham/0004.1999-12-14.farmer.ham.txt"
abs_file_path = os.path.join('ham', '0002.1999-12-13.farmer.ham.txt')

f = open(rel_path, "r")
content = f.read()

# transform the string into lower and then split
print(content)
