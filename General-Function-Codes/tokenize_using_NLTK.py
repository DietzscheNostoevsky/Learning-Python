#!/usr/bin/env python
import os
import nltk


file_content = open(
    "/Users/saurabhkumarsingh/Documents/GitHub/Learning-Python/Course-1/Week 6/Word_cloud/testfile.txt").read()
tokens = nltk.word_tokenize(file_content)
print(tokens)
