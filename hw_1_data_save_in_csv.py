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

text_content_train = []
topicname_list_train = []


text_content_test = []
topicname_list_test = []



def get_article_by_bs4() -> None:
    """
    get reuters aritcle example code
    :return: None because example code
    """
    dataDir = "./"  # If you are in the same directory, you can use "./"
    # dataDir = "YOUR_FILE_DIRECTORY"  # If you are in the same directory, you can use "./"
    sgmlFileFormat = dataDir + "reut2-{}.sgm"

    for fileIdx in range(0, 22):  # 22 last
        # Get file IO stream
        f: TextIO = open(sgmlFileFormat.format(str(fileIdx).zfill(3)), 'r')
        content: str = f.read()
        f.close()

        # Parsing
        bs = BeautifulSoup(content, 'lxml')
        reuters: List[bs4.element.Tag] = bs.find_all('reuters')
        for article in reuters:
             # TOPICS = "YES"
            # LEWISSPLIT = "TRAIN"
            topic: str = article['topics']
            lewissplit: str = article['lewissplit']

            # print("article ", article)


            newId: str = article['newid']
            oldId: str = article['oldid']
            textTag = article.find('text')
            # print("textTag ", textTag)


            topicD = article.find('topics')
            # print("topicD ", topicD)

            try:
                title: str = textTag.find('title').get_text().strip()
            except AttributeError:  # no title content
                title: str = ''
            try:
                topicname: str = topicD.find('d').get_text().strip()
            except AttributeError:  # no topic content
                topicname: str = ''

            # try:
            #     dateline: str = textTag.find('dateline').get_text().strip()
            # except AttributeError:  # no topic content
            #     dateline: str = ''

            # print("NEWID : {}, OLDID : {}, TITLE : {} ".format(newId, oldId, title))
            # print("topicname ", topicname)
            # print("NEWID : {}, OLDID : {}, TITLE : {}, TOPICS: {}".format(newId, oldId, title, topicname))
            # print("NEWID : {}, OLDID : {}, TITLE : {}, TOPICS_NAME: {}, TOPICS: {}, LEWISSPLIT: {}".format(newId, oldId,
            #                                                                                                title,
            #                                                                                                topicname,
            #                                                                                                topic,
            #                                                                                                lewissplit))
            if topic == "YES" and lewissplit == "TRAIN" and topicname != "":
                print("NEWID : {}, OLDID : {}, TITLE : {}, TOPICS_NAME: {}, TOPICS: {}, LEWISSPLIT: {}".format(newId, oldId, title, topicname, topic, lewissplit))
                # print("TITLE : {}, TOPICS_NAME: {}".format(title, topicname))
                # print("TITLE :", title)
                # print("dateline :", dateline)
                # with open("train_data.sgm", "a") as myfile:
                #     myfile.write(str(article))
                #     myfile.write("\n")
                text_content_train.append(textTag)
                topicname_list_train.append(topicname)

            if topic == "YES" and lewissplit == "TEST" and topicname != "":
                print("NEWID : {}, OLDID : {}, TITLE : {}, TOPICS_NAME: {}, TOPICS: {}, LEWISSPLIT: {}".format(newId, oldId, title, topicname, topic, lewissplit))
                # with open("test_data.sgm", "a") as myfile:
                #     myfile.write(str(article))
                #     myfile.write("\n")
                text_content_test.append(textTag)
                topicname_list_test.append(topicname)



if __name__ == "__main__":
    get_article_by_bs4()
    dict_train = {'text': text_content_train,
            'topicname': topicname_list_train}
    csv_df_train = pd.DataFrame(dict_train)
    # saving the dataframe
    csv_df_train.to_csv("all_data/train_data_all.csv", encoding='utf-8', index=False)

    dict_test = {'text': text_content_test,
            'topicname': topicname_list_test}
    csv_df_test = pd.DataFrame(dict_test)
    # saving the dataframe
    csv_df_test.to_csv("all_data/test_data_all.csv", encoding='utf-8', index=False)