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


# data = pd.read_csv("all_data/train_data_all.csv", nrows=603)

# data = pd.read_csv("all_data/test_data_all.csv",nrows=299)

# data = pd.read_csv("all_data/train_data_all.csv")

data = pd.read_csv("all_data/test_data_all.csv")

# data.dropna()

print(data.head())

topic_name_df = data["topicname"]
list_topic_name = topic_name_df.values.tolist()
print("list_topic_name ",list_topic_name)

# count_list = Counter(list_topic_name).values()
# print("count_list ",count_list)


def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    # for key, value in freq.items():
        # print("% d : % d" % (key, value))
        # print("key ", key, "value ", value)
        # print( key, ":", value)

    return freq

# my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
#
# CountFrequency(my_list)

freq_dic_topic = CountFrequency(list_topic_name)

print("freq_dic_topic =",freq_dic_topic)

import operator
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(freq_dic_topic.items(), reverse=True, key=operator.itemgetter(1))
# sorted_x = sorted(freq_dic_topic.items(), reverse=False, key=operator.itemgetter(1))
print("sorted_x =", sorted_x)

# mydict = {1:'a',2:'b',3:'c',4:'d',5:'e'}

mydict = dict(sorted_x)
print("mydict ", mydict)
for x in list(mydict)[0:10]:
    print (mydict[x])




# def add(self, key, value):
#     self[key] = value

# while (ii < 10):
#     ii+=1
#     print("ii :", ii)
    # print("mydict.popitem() ", mydict.popitem())
    # new_dic_for_10_class.add(mydict.popitem())

# print("new_dic_for_10_class = ", new_dic_for_10_class)
# for key, value in mydict.items():
#     ii += 1
#     print("key ", key, "value ", value)
#     new_dic_for_10_class[key] = value
#     if ii ==10:
#         print("new_dic_for_10_class = ", new_dic_for_10_class)
#         break

top_10_class_list = []

def read_top_10_class_name ():
    ii = 0
    new_dic_for_10_class = dict()
    for key, value in mydict.items():
        ii += 1
        print("key ", key, "value ", value)
        new_dic_for_10_class[key] = value
        top_10_class_list.append(key)
        if ii == 10:
            print("new_dic_for_10_class = ", new_dic_for_10_class)
            return new_dic_for_10_class

new_dic_for_10_class = read_top_10_class_name()
print("new_dic_for_10_class = ", new_dic_for_10_class)
print("top_10_class_list =", top_10_class_list)
# import collections
# sorted_dict = collections.OrderedDict(sorted_x)
# print("sorted_dict =", sorted_dict)

# for i in range(len(data)):
#     print(data.loc[i, "title"], data.loc[i, "topicname"])

topic_text_list = []
topic_name_list = []
topic_label_list = []

top_10_class_list = ['earn', 'acq', 'money-fx', 'grain', 'crude', 'trade', 'interest', 'ship', 'money-supply', 'sugar'] #open this one for test data label

for ind in data.index:
     # print(data['title'][ind], data['topicname'][ind])
     if data['topicname'][ind] == top_10_class_list[0]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(0)

     if data['topicname'][ind] == top_10_class_list[1]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(1)

     if data['topicname'][ind] == top_10_class_list[2]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(2)

     if data['topicname'][ind] == top_10_class_list[3]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(3)

     if data['topicname'][ind] == top_10_class_list[4]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(4)

     if data['topicname'][ind] == top_10_class_list[4]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(4)

     if data['topicname'][ind] == top_10_class_list[5]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(5)

     if data['topicname'][ind] == top_10_class_list[6]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(6)

     if data['topicname'][ind] == top_10_class_list[7]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(7)

     if data['topicname'][ind] == top_10_class_list[8]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(8)

     if data['topicname'][ind] == top_10_class_list[9]:
         topic_text_list.append(data['text'][ind])
         topic_name_list.append(data['topicname'][ind])
         topic_label_list.append(9)


     # if data['topicname'][ind] == "earn" or data['topicname'][ind] == "acq" or data['topicname'][ind] == "crude" or data['topicname'][ind] == "money-supply"\
     #         or data['topicname'][ind] == "grain" or data['topicname'][ind] == "money-fx" or data['topicname'][ind] == "coffee" or data['topicname'][ind] == "trade" \
     #         or data['topicname'][ind] == "veg-oil" or data['topicname'][ind] == "reserves":
     #     topic_text_list.append(data['title'][ind])
     #     topic_name_list.append(data['topicname'][ind])
         # print(data["topicname: ", data['topicname'][ind])


print("len(topic_name_list) = ",len(topic_name_list))


# for row in data.iterrows():
#     print(row['title'], row['topicname'])


dict = {'text': topic_text_list,
        'topicname': topic_name_list,
        'label': topic_label_list}
csv_df = pd.DataFrame(dict)
# saving the dataframe
# csv_df.to_csv("all_data/train_all_data_label.csv", encoding='utf-8', index=False) #open this one for train data label save

csv_df.to_csv("all_data/test_all_data_label.csv", encoding='utf-8', index=False) #open this one for test data label save