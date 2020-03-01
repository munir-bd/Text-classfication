import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from typing import TextIO
from bs4 import BeautifulSoup
import re
import math
import itertools
import copy
from collections import Counter



data = pd.read_csv("all_data/train_all_data_label.csv")

print("len(data) ", len(data))

data_test = pd.read_csv("all_data/test_all_data_label.csv")

print("len(data_test) ", len(data_test))

# data.dropna()

print(data.head())

# data['label'] = data["topicname"].apply(lambda x: 0 if x=="earn" else 1)

print(data.head())

from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(data["text"], data["label"], random_state=1)

X_train = data["text"].values
y_train = data["label"].values

X_test =  data_test["text"].values
y_test =  data_test["label"].values


# print("X_train = ", X_train)
# print("y_train = ", y_train)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(strip_accents="ascii", token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True, stop_words='english')

X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)

# print("X_train_cv = ", X_train_cv)
# print("y_train = ", y_train)

word_freq_df = pd.DataFrame(X_train_cv.toarray(), columns=cv.get_feature_names())

top_words_df = pd.DataFrame(word_freq_df.sum()).sort_values(0, ascending=False)

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_cv, y_train)
predictions = naive_bayes.predict(X_test_cv)

from sklearn.metrics import accuracy_score
print( 'Accuracy score: ', accuracy_score(y_test, predictions))

print("y_test = ", y_test)
print("predictions = ", predictions)

top_10_class_list = ['earn', 'acq', 'crude', 'grain', 'money-supply', 'money-fx', 'coffee', 'trade', 'veg-oil', 'interest']

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
cm = confusion_matrix(y_test, predictions)
print("cm ", cm)
sns.heatmap(cm, square=True, annot=True, cmap='Blues_r', cbar=False,
xticklabels=[top_10_class_list], yticklabels=[top_10_class_list])
plt.xlabel('true label')
plt.ylabel('predicted label')

plt.show()

