from gensim.models import word2vec, KeyedVectors
import numpy as np
import pickle
from scipy import io
from tqdm import tqdm

def cos_sim(vec1, vec2):
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return -1
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

with open('section09/matrix_key', 'rb') as f:
    keys = pickle.load(f)

matrix_300 = io.loadmat("section09/matrix_300")['matrix']

model = KeyedVectors.load_word2vec_format('section10/matrix_word2vec.txt', binary=True)

with open('section10/wordsim353/combined.tab', 'rt') as f, \
    open('section10/combined90.tab', 'wt') as g:
    flag = True
    for line in tqdm(f.readlines()):
        if flag:
            flag = False
            continue
        line = line.split()
        w0 = line[0]
        w1 = line[1]
        #90
        try:
            vec1 = model[w0]
            vec2 = model[w1]
            score = cos_sim(vec1, vec2)
            g.write("{} {} {}\n".format(w0, w1, score))
        except KeyError:
            g.write("{} {} {}\n".format(w0, w1, -1))

with open('section10/wordsim353/combined.tab', 'rt') as f, \
    open('section10/combined85.tab', 'wt') as g:
    flag = True
    for line in tqdm(f.readlines()):
        if flag:
            flag = False
            continue
        line = line.split()
        w0 = line[0]
        w1 = line[1]
        try:
            vec1 = matrix_300[keys[w0]]
            vec2 = matrix_300[keys[w1]]
            score = cos_sim(vec1, vec2)
            g.write("{} {} {}\n".format(w0, w1, score))
        except KeyError:
            g.write("{} {} {}\n".format(w0, w1, -1))