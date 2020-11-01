import csv
import sys
csv.field_size_limit(sys.maxsize)
import pickle
import re
from os import walk
from random import random

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier

from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import seaborn as sns


arr = []

print("Hello World")
mypath = "./blog/test/test2/"

d = []
for (dirpath, dirnames, filenames) in walk(mypath):
    d.extend(filenames)
    break

for file in d:
    with open(mypath + file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        for d in data:
            gender = d[1]
            age = int(d[2])

            if age < 20:
                age = 0
            elif age < 30:
                age = 1
            else:
                age = 2

            zodiac = d[3]
            text = d[4]

            data_arr = [gender, age, zodiac, text]
            arr.append(data_arr)

with open('test2.pkl', 'wb') as f:
    pickle.dump(arr, f)

print("Bye World")
