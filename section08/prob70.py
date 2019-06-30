import random

path_pos = 'section8/rt-polaritydata/rt-polaritydata/rt-polarity.pos'
path_neg = 'section8/rt-polaritydata/rt-polaritydata/rt-polarity.neg'
path_smt = 'section8/sentiment.txt'

list_pos = []
list_neg = []
num_pos = 0
num_neg = 0

with open(path_pos, encoding='cp1252') as f:
    for text in f:
        num_pos += 1
        list_pos.append(str("+1 "+text))

with open(path_neg, encoding='cp1252') as f:
    for text in f:
        num_neg += 1
        list_neg.append(str("-1 "+text))

list_sent = list_pos + list_neg
random.shuffle(list_sent)

with open(path_smt, 'w') as output:
    for sent in list_sent:
        output.write(sent)

print('pos:{}, neg:{}'.format(num_pos, num_neg))