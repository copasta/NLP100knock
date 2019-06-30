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
from sklearn.model_selection import StratifiedKFold

X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.3, random_state=1234)
print(X_train.shape, X_test.shape)

folds = StratifiedKFold(n_splits=5, random_state=1007)

oof_preds = np.zeros(X_train.shape[0])
sub_preds = np.zeros(X_test.shape[0])

for n_fold, (train_idx, val_idx) in enumerate(folds.split(X_train, y_train)):
    train_x, train_y = X_train[train_idx], y_train[train_idx]
    val_x, val_y = X_train[val_idx], y_train[val_idx]

    model = LogisticRegression(solver='lbfgs', random_state=(1234 + n_fold))
    model.fit(train_x, train_y)

    oof_preds[val_idx] = model.predict(val_x)
    sub_preds += model.predict(X_test) / folds.n_splits

print('val accuracy :{} \t test  accuracy :{}'.format(accuracy(y_train, oof_preds), accuracy(y_test, sub_preds)))
print('val precision:{} \t test  precision:{}'.format(precision(y_train, oof_preds), precision(y_test, sub_preds)))
print('cal recall   :{} \t test  recall   :{}'.format(recall(y_train, oof_preds), recall(y_test, sub_preds)))
print('val f1 score :{} \t test  f1 score :{}'.format(f1_score(y_train, oof_preds), f1_score(y_test, sub_preds)))

