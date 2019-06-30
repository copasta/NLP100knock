
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer # 精度がイマイチ
from stemming.porter2 import stem # こっちも怪しい
import pandas as pd
import numpy as np
import pickle

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

print(X.shape)
print(label.shape)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, label, test_size=0.3, random_state=1234)

model = LogisticRegression(solver='lbfgs', random_state=1234)
model.fit(X_train, y_train)
w_path = 'section8/weight.csv'
pickle.dump(model, open(w_path, 'wb'))