import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer # 精度がイマイチ
from stemming.porter2 import stem # こっちも怪しい
import pandas as pd
import numpy as np
import pickle

def confusion_matrix(y_true, y_pred):
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for t, p in zip(y_true, y_pred):
        if t == p and t == 1:
            TP += 1
        elif t == p and t == 0:
            TN += 1
        elif t != p and t == 1:
            FN += 1
        elif t != p and t == 0:
            FP += 1
    return TP, FP, TN, FN

def accuracy(y_true, y_pred):
    TP, FP, TN, FN = confusion_matrix(y_true, y_pred)
    acc = (TP + TN) / (TP + FP + TN + FN)
    return acc

def precision(y_true, y_pred):
    TP, FP, TN, FN = confusion_matrix(y_true, y_pred)
    prec = TP / (TP + FP)
    return prec

def recall(y_true, y_pred):
    TP, FP, TN, FN = confusion_matrix(y_true, y_pred)
    rec = TP / (TP + FN)
    return rec

def f1_score(y_true, y_pred):
    rec = recall(y_true, y_pred)
    prec = precision(y_true, y_pred)
    return (2 * rec * prec) / (rec + prec)

path = 'section8/sentiment.txt'

list_stop = [x for x in stopwords.words('english')]

label = []
sent = []

with open(path) as f:
    for line in f.readlines():
        l = int(line[:2])
        if l == -1:
            label.append(0)
        else:
            label.append(l)
        s = line[3:].replace(',', '').replace('.', '').split()
        temp = []
        for ss in s:
            temp.append(stem(ss))
        sent.append(" ".join(temp))
label = np.array(label)

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(stop_words=list_stop)
X = vectorizer.fit_transform(sent)
feature = vectorizer.get_feature_names()

print(X.shape)
print(label.shape)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.3, random_state=1234)

w_path = 'section8/weight.csv'
model = pickle.load(open(w_path, 'rb'))
y_pred = model.predict(X_test)

print('accuracy: {}'.format(accuracy(y_test, y_pred)))
print('precision:{}'.format(precision(y_test, y_pred)))
print('recall:   {}'.format(recall(y_test, y_pred)))
print('f1 score: {}'.format(f1_score(y_test, y_pred)))

