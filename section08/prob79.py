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

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold

X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.3, random_state=1234)
print(X_train.shape, X_test.shape)

folds = StratifiedKFold(n_splits=5, random_state=1007)

sub_preds = np.zeros(X_test.shape[0])

for n_fold, (train_idx, val_idx) in enumerate(folds.split(X_train, y_train)):
    train_x, train_y = X_train[train_idx], y_train[train_idx]
    val_x, val_y = X_train[val_idx], y_train[val_idx]

    model = LogisticRegression(solver='lbfgs', random_state=(1234 + n_fold))
    model.fit(train_x, train_y)
    
    pred = model.predict_proba(X_test)[:, 0]
    sub_preds += pred / folds.n_splits

delta = np.arange(0.02, 1.0, 0.02).reshape(-1, 1)
acc = np.zeros((delta.shape[0], 1))
prec = np.zeros((delta.shape[0], 1))
rec = np.zeros((delta.shape[0], 1))
f1 = np.zeros((delta.shape[0], 1))

idx = 0

for th in delta:
    test_pred = (sub_preds > th).astype(int)
    acc[idx] = accuracy(y_test, test_pred)
    prec[idx] = precision(y_test, test_pred)
    rec[idx] = recall(y_test, test_pred)
    f1[idx] = f1_score(y_test, test_pred)
    idx += 1

import matplotlib.pyplot as plt

plt.figure()
plt.plot(delta, acc, label='accuray')
plt.plot(delta, prec, label='precision')
plt.plot(delta, rec, label='recall')
plt.plot(delta, f1, label='f1 score')
plt.legend()
plt.xlabel('delta')
plt.savefig('section8/prob79.png')
