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

with open('section10/family.txt', 'rt') as f, \
    open('section10/family90.txt', 'wt') as g:
    for line in tqdm(f.readlines()):
        line = line.split()
        w0 = line[0]
        w1 = line[1]
        w2 = line[2]
        w3 = line[3]
        #90
        try:
            w_sim, score = model.most_similar(positive=[w1, w2], negative=[w0], topn=1)[0]
            g.write("{} {} {} {} {} {}\n".format(w0, w1, w2, w3, w_sim, score))
        except KeyError:
            g.write("{} {} {} {} N/A {}\n".format(w0, w1, w2, w3, -1))

with open('section10/family.txt', 'rt') as f, \
    open('section10/family85.txt', 'wt') as g:
    for line in tqdm(f.readlines()):
        line = line.split()
        w0 = line[0]
        w1 = line[1]
        w2 = line[2]
        w3 = line[3]
        try:
            vec = matrix_300[keys[w1]] - matrix_300[keys[w0]] + matrix_300[keys[w2]]
            sim_dic = {}
            for key, value in keys.items():
                sim_dic[key] = cos_sim(vec, matrix_300[value])
            sim_dic = sorted(sim_dic.items(), key=lambda x:x[1], reverse=True)
            w_sim, score = sim_dic[0]
            g.write("{} {} {} {} {} {}\n".format(w0, w1, w2, w3, w_sim, score))
        except KeyError:
            g.write("{} {} {} {} N/A {}\n".format(w0, w1, w2, w3, -1))