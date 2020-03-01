# Md Shirajum Munir (2017310936)
#
# I have taken help from this site : https://www.python-course.eu/text_classification_python.php
# for Naive Bayes classifier


import re, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class BagOfWords(object):
    """ Implementing a bag of words, words corresponding with their frequency of usages in a "document"
    for usage by the Document class, DocumentClass class and the Pool class."""

    def __init__(self):
        self.__number_of_words = 0
        self.__bag_of_words = {}

    def __add__(self, other):
        """ Overloading of the "+" operator to join two BagOfWords """
        erg = BagOfWords()
        sum = erg.__bag_of_words
        for key in self.__bag_of_words:
            sum[key] = self.__bag_of_words[key]
            if key in other.__bag_of_words:
                sum[key] += other.__bag_of_words[key]
        for key in other.__bag_of_words:
            if key not in sum:
                sum[key] = other.__bag_of_words[key]
        return erg

    def add_word(self, word):
        """ A word is added in the dictionary __bag_of_words"""
        self.__number_of_words += 1
        if word in self.__bag_of_words:
            self.__bag_of_words[word] += 1
        else:
            self.__bag_of_words[word] = 1

    def len(self):
        """ Returning the number of different words of an object """
        return len(self.__bag_of_words)

    def Words(self):
        """ Returning a list of the words contained in the object """
        return self.__bag_of_words.keys()

    def BagOfWords(self):
        """ Returning the dictionary, containing the words (keys) with their frequency (values)"""
        return self.__bag_of_words

    def WordFreq(self, word):
        """ Returning the frequency of a word """
        if word in self.__bag_of_words:
            return self.__bag_of_words[word]
        else:
            return 0


class Document(object):
    """ Used both for learning (training) documents and for testing documents. The optional parameter lear
    has to be set to True, if a classificator should be trained. If it is a test document learn has to be set to False. """
    _vocabulary = BagOfWords()

    def __init__(self, vocabulary):
        self.__name = ""
        self.__document_class = None
        self._words_and_freq = BagOfWords()
        Document._vocabulary = vocabulary


    def add_text_to_doc(self, text, learn=False):
        text = text.lower()
        words = re.split(r"\W", text)

        self._number_of_words = 0
        for word in words:
            self._words_and_freq.add_word(word)
            if learn:
                Document._vocabulary.add_word(word)

    def __add__(self, other):
        """ Overloading the "+" operator. Adding two documents consists in adding the BagOfWords of the Documents """
        res = Document(Document._vocabulary)
        res._words_and_freq = self._words_and_freq + other._words_and_freq
        return res

    def vocabulary_length(self):
        """ Returning the length of the vocabulary """
        return len(Document._vocabulary)

    def WordsAndFreq(self):
        """ Returning the dictionary, containing the words (keys) with their frequency (values) as contained
        in the BagOfWords attribute of the document"""
        return self._words_and_freq.BagOfWords()

    def Words(self):
        """ Returning the words of the Document object """
        d = self._words_and_freq.BagOfWords()
        return d.keys()

    def WordFreq(self, word):
        """ Returning the number of times the word "word" appeared in the document """
        bow = self._words_and_freq.BagOfWords()
        if word in bow:
            return bow[word]
        else:
            return 0

    def __and__(self, other):
        """ Intersection of two documents. A list of words occuring in both documents is returned """
        intersection = []
        words1 = self.Words()
        for word in other.Words():
            if word in words1:
                intersection += [word]
        return intersection


class DocumentClass(Document):
    def __init__(self, vocabulary):
        Document.__init__(self, vocabulary)
        self._number_of_docs = 0

    def Probability(self, word):
        """ returns the probabilty of the word "word" given the class "self" """
        voc_len = Document._vocabulary.len()
        SumN = 0
        for i in range(voc_len):
            SumN = DocumentClass._vocabulary.WordFreq(word)
        N = self._words_and_freq.WordFreq(word)
        erg = 1 + N
        erg /= voc_len + SumN
        return erg

    def __add__(self, other):
        """ Overloading the "+" operator. Adding two DocumentClass objects consists in adding the
        BagOfWords of the DocumentClass objectss """
        res = DocumentClass(self._vocabulary)
        res._words_and_freq = self._words_and_freq + other._words_and_freq

        return res

    def SetNumberOfDocs(self, number):
        self._number_of_docs = number

    def NumberOfDocuments(self):
        return self._number_of_docs


class Pool(object):
    def __init__(self):
        self.__document_classes = {}
        self.__vocabulary = BagOfWords()

    def sum_words_in_class(self, dclass):
        """ The number of times all different words of a dclass appear in a class """
        sum = 0
        for word in self.__vocabulary.Words():
            WaF = self.__document_classes[dclass].WordsAndFreq()
            if word in WaF:
                sum += WaF[word]
        return sum

    def learn(self, directory, dclass_name):
        """ directory is a path, where the files of the class with the name dclass_name can be found """
        print("directory ", directory)
        print("dclass_name ", dclass_name)

        data = pd.read_csv(directory+".csv")
        # data.dropna()
        print(data.head())
        # topic_name_df = data["topicname"]
        # list_topic_name = topic_name_df.values.tolist()
        # print("list_topic_name ", list_topic_name)

        x = DocumentClass(self.__vocabulary)
        print("x ", x)

        for i in range(len(data)):
            # print(data.loc[i, "text"], data.loc[i, "topicname"])
            d = Document(self.__vocabulary)
            d.add_text_to_doc(data.loc[i, "text"], learn=True)
            x = x + d
        self.__document_classes[dclass_name] = x
        x.SetNumberOfDocs(len(data))


    def Probability(self, doc, dclass=""):
        """Calculates the probability for a class dclass given a document doc"""
        if dclass:
            sum_dclass = self.sum_words_in_class(dclass)
            prob = 0

            d = Document(self.__vocabulary)
            d.add_text_to_doc(doc)

            for j in self.__document_classes:
                sum_j = self.sum_words_in_class(j)
                prod = 1
                for i in d.Words():
                    wf_dclass = 1 + self.__document_classes[dclass].WordFreq(i)
                    wf = 1 + self.__document_classes[j].WordFreq(i)
                    r = wf * sum_dclass / (wf_dclass * sum_j)
                    prod *= r
                prob += prod * self.__document_classes[j].NumberOfDocuments() / self.__document_classes[
                    dclass].NumberOfDocuments()
            if prob != 0:
                return 1 / prob
            else:
                return -1
        else:
            prob_list = []
            for dclass in self.__document_classes:
                prob = self.Probability(doc, dclass)
                prob_list.append([dclass, prob])
            prob_list.sort(key=lambda x: x[1], reverse=True)
            return prob_list

    def DocumentIntersectionWithClasses(self, doc_name):
        res = [doc_name]
        for dc in self.__document_classes:
            d = Document(self.__vocabulary)
            d.add_text_to_doc(doc_name, learn=False)
            o = self.__document_classes[dc] & d
            intersection_ratio = len(o) / len(d.Words())
            res += (dc, intersection_ratio)
        return res



DClasses = ['earn', 'acq', 'money-fx', 'grain', 'crude', 'trade', 'interest', 'ship', 'money-supply', 'sugar']

# base = "learn_and_test_debug/learn/"
# base = "learn_and_test/learn/"

base = "all_data/my_data/train/"
p = Pool()
for i in DClasses:
    print("i ", i)
    p.learn(base + i, i)


true_list = []
predict_list = []
true_label_list = []
pred_label_list = []


base = "all_data/my_data/test/"
for ii in DClasses:
    data = pd.read_csv(base+ii + ".csv")
    for i in range(len(data)):
        res = p.Probability(data.loc[i, "text"])
        true_list.append(data.loc[i, "topicname"])
        true_label_list.append(data.loc[i, "label"])
        pred_item = (res[0])
        predict_list.append(pred_item[0])
        # print("pred_item ",pred_item[0])
        for lb_ind in range (len(DClasses)):
            if DClasses[lb_ind] == pred_item[0]:
                # print("lb_ind ", lb_ind)
                pred_label_list.append(lb_ind)



        # print(data.loc[i, "topicname"] +" : ", str(res[0]))
        # print( str(res))
        # print(data.loc[i, "topicname"] + " : ", str(res))
        with open("output_final.txt", "a") as myfile:
            myfile.write(data.loc[i, "topicname"] + " : "+ str(res)+"\n")

print("true_list ",true_list)
print("predict_list ",predict_list)
print("true_label_list =",true_label_list)
print("pred_label_list =", pred_label_list)

from sklearn.metrics import accuracy_score, precision_score, recall_score
print( 'Accuracy score: ', accuracy_score(true_label_list, pred_label_list))
# print( "Precision score: ", precision_score(true_label_list, pred_label_list))
# print("Recall score: ", recall_score(true_label_list, pred_label_list))


top_10_class_list = ['earn', 'acq', 'money-fx', 'grain', 'crude', 'trade', 'interest', 'ship', 'money-supply', 'sugar']

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
cm = confusion_matrix(true_label_list, pred_label_list)
sns.heatmap(cm, square=True, annot=True, cmap='GnBu', cbar=False,
xticklabels=[top_10_class_list], yticklabels=[top_10_class_list])
plt.xlabel('true label')
plt.ylabel('predicted label')

plt.show()