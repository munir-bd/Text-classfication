# Text-classfication
Naïve-Bayes Classifier on the Reuters-21578 dataset. NaiveBayes implementation with and without sklearn lib.
Write a program for classfication using the Naïve-Bayes Classifier on
the Reuters-21578 dataset. For the topic classes, consider only top ten 
classes w.r.t. topic frequency. Ignore all other topics.


1. hw_1_data_save_in_csv.py 
hw_1_data_save_in_csv.py file is used for training and testing
date separation from Reuters-21578 dataset using the example code.
Here, we create to separate csv file using   topic == "YES" and lewissplit == "TRAIN" and topicname != "":
and topic == "YES" and lewissplit == "TEST" and topicname != "":.
out put from hw_1_data_save_in_csv.py
all_data/train_data_all
all_data/test_data_all.csv


2. hw_1_preprocess_with_10_class.py
3. hw_1_testing_preprocessing.py
Code 2 and 3 is used for 10 types of document separation for training and testing.
all_data/my_data/train/* output form hw_1_preprocess_with_10_class.py
all_data/my_data/test/* output form hw_1_testing_preprocessing.py



4. hw_1_NaiveBayes.py
This code used for NaiveBayes implementation for training, and testing.
I have taken help from: https://www.python-course.eu/text_classification_python.php

5. hw_1_preprocess_label_add.py
This code is used for label generation in numerical value for top 10 topics.

6. hw_1_Lib_NaiveBayes.py
We test using NaiveBayes sklearn lib in file hw_1_Lib_NaiveBayes.py

7. hw_1_doc_claas_fig_gen.py
This file used for fig generation.

8. result_Final.txt file contain the output log of all results.
