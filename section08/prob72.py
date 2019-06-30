
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer # 精度がイマイチ
from stemming.porter2 import stem # こっちも怪しい

path = 'section8/sentiment.txt'

list_stop = [x for x in stopwords.words('english')]

label = []
sent = []

with open(path) as f:
    for line in f.readlines():
        label.append(int(line[:2]))
        s = line[3:].replace(',', '').replace('.', '').split()
        temp = []
        for ss in s:
            if ss not in list_stop:
                temp.append(stem(ss))
        sent.append(temp)
print(sent[10])
print(label[10])