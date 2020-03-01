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


# data = pd.read_csv("all_data/train_data_all.csv", nrows=603) #use for train generation and nrows=603 according to ppt
# data = pd.read_csv("all_data/test_data_all.csv", nrows=299) #use for test generation and nrows=603 299 to ppt

data = pd.read_csv("all_data/train_data_all.csv")
# data = pd.read_csv("all_data/test_data_all.csv")
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

topic_text_list_1 = []
topic_name_list_1 = []
topic_label_list_1 = []

topic_text_list_2 = []
topic_name_list_2 = []
topic_label_list_2 = []

topic_text_list_3 = []
topic_name_list_3 = []
topic_label_list_3 = []

topic_text_list_4 = []
topic_name_list_4 = []
topic_label_list_4 = []

topic_text_list_5 = []
topic_name_list_5 = []
topic_label_list_5 = []

topic_text_list_6 = []
topic_name_list_6 = []
topic_label_list_6 = []

topic_text_list_7 = []
topic_name_list_7 = []
topic_label_list_7 = []

topic_text_list_8 = []
topic_name_list_8 = []
topic_label_list_8 = []

topic_text_list_9 = []
topic_name_list_9 = []
topic_label_list_9 = []

topic_text_list_10 = []
topic_name_list_10 = []
topic_label_list_10 = []

for ind in data.index:
     # print(data['text'][ind], data['topicname'][ind])
     if data['topicname'][ind] == top_10_class_list[0]:
         topic_text_list_1.append(data['text'][ind])
         topic_name_list_1.append(data['topicname'][ind])
         topic_label_list_1.append(0)

     if data['topicname'][ind] == top_10_class_list[1]:
         topic_text_list_2.append(data['text'][ind])
         topic_name_list_2.append(data['topicname'][ind])
         topic_label_list_2.append(1)

     if data['topicname'][ind] == top_10_class_list[2]:
         topic_text_list_3.append(data['text'][ind])
         topic_name_list_3.append(data['topicname'][ind])
         topic_label_list_3.append(2)

     if data['topicname'][ind] == top_10_class_list[3]:
         topic_text_list_4.append(data['text'][ind])
         topic_name_list_4.append(data['topicname'][ind])
         topic_label_list_4.append(3)

     if data['topicname'][ind] == top_10_class_list[4]:
         topic_text_list_5.append(data['text'][ind])
         topic_name_list_5.append(data['topicname'][ind])
         topic_label_list_5.append(4)

     if data['topicname'][ind] == top_10_class_list[5]:
         topic_text_list_6.append(data['text'][ind])
         topic_name_list_6.append(data['topicname'][ind])
         topic_label_list_6.append(5)

     if data['topicname'][ind] == top_10_class_list[6]:
         topic_text_list_7.append(data['text'][ind])
         topic_name_list_7.append(data['topicname'][ind])
         topic_label_list_7.append(6)

     if data['topicname'][ind] == top_10_class_list[7]:
         topic_text_list_8.append(data['text'][ind])
         topic_name_list_8.append(data['topicname'][ind])
         topic_label_list_8.append(7)

     if data['topicname'][ind] == top_10_class_list[8]:
         topic_text_list_9.append(data['text'][ind])
         topic_name_list_9.append(data['topicname'][ind])
         topic_label_list_9.append(8)

     if data['topicname'][ind] == top_10_class_list[9]:
         topic_text_list_10.append(data['text'][ind])
         topic_name_list_10.append(data['topicname'][ind])
         topic_label_list_10.append(9)


     # if data['topicname'][ind] == "earn" or data['topicname'][ind] == "acq" or data['topicname'][ind] == "crude" or data['topicname'][ind] == "money-supply"\
     #         or data['topicname'][ind] == "grain" or data['topicname'][ind] == "money-fx" or data['topicname'][ind] == "coffee" or data['topicname'][ind] == "trade" \
     #         or data['topicname'][ind] == "veg-oil" or data['topicname'][ind] == "reserves":
     #     topic_text_list.append(data['text'][ind])
     #     topic_name_list.append(data['topicname'][ind])
         # print(data["topicname: ", data['topicname'][ind])


# print("len(topic_name_list) = ",len(topic_name_list))


# for row in data.iterrows():
#     print(row['text'], row['topicname'])
loc = "all_data/my_data/train/" #use for train generation
# loc = "all_data/my_data/test/" #use for test genration

dict_1 = {'text': topic_text_list_1,
        'topicname': topic_name_list_1,
        'label': topic_label_list_1}
csv_df_1 = pd.DataFrame(dict_1)
# saving the dataframe
csv_df_1.to_csv(loc+top_10_class_list[0]+".csv", encoding='utf-8', index=False)

dict_2 = {'text': topic_text_list_2,
        'topicname': topic_name_list_2,
        'label': topic_label_list_2}
csv_df_2 = pd.DataFrame(dict_2)
# saving the dataframe
csv_df_2.to_csv(loc+top_10_class_list[1]+".csv", encoding='utf-8', index=False)

dict_3 = {'text': topic_text_list_3,
        'topicname': topic_name_list_3,
        'label': topic_label_list_3}
csv_df_3 = pd.DataFrame(dict_3)
# saving the dataframe
csv_df_3.to_csv(loc+top_10_class_list[2]+".csv", encoding='utf-8', index=False)

dict_4 = {'text': topic_text_list_4,
        'topicname': topic_name_list_4,
        'label': topic_label_list_4}
csv_df_4 = pd.DataFrame(dict_4)
# saving the dataframe
csv_df_4.to_csv(loc+top_10_class_list[3]+".csv", encoding='utf-8', index=False)

dict_5 = {'text': topic_text_list_5,
        'topicname': topic_name_list_5,
        'label': topic_label_list_5}
csv_df_5 = pd.DataFrame(dict_5)
# saving the dataframe
csv_df_5.to_csv(loc+top_10_class_list[4]+".csv", encoding='utf-8', index=False)

dict_6 = {'text': topic_text_list_6,
        'topicname': topic_name_list_6,
        'label': topic_label_list_6}
csv_df_6 = pd.DataFrame(dict_6)
# saving the dataframe
csv_df_6.to_csv(loc+top_10_class_list[5]+".csv", encoding='utf-8', index=False)

dict_7 = {'text': topic_text_list_7,
        'topicname': topic_name_list_7,
        'label': topic_label_list_7}
csv_df_7 = pd.DataFrame(dict_7)
# saving the dataframe
csv_df_7.to_csv(loc+top_10_class_list[6]+".csv", encoding='utf-8', index=False)

dict_8 = {'text': topic_text_list_8,
        'topicname': topic_name_list_8,
        'label': topic_label_list_8}
csv_df_8 = pd.DataFrame(dict_8)
# saving the dataframe
csv_df_8.to_csv(loc+top_10_class_list[7]+".csv", encoding='utf-8', index=False)

dict_9 = {'text': topic_text_list_9,
        'topicname': topic_name_list_9,
        'label': topic_label_list_9}
csv_df_9 = pd.DataFrame(dict_9)
# saving the dataframe
csv_df_9.to_csv(loc+top_10_class_list[8]+".csv", encoding='utf-8', index=False)

dict_10 = {'text': topic_text_list_10,
        'topicname': topic_name_list_10,
        'label': topic_label_list_10}
csv_df_10 = pd.DataFrame(dict_10)
# saving the dataframe
csv_df_10.to_csv(loc+top_10_class_list[9]+".csv", encoding='utf-8', index=False)