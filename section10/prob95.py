from gensim.models import word2vec, KeyedVectors
import numpy as np
import pickle
from scipy import io
from tqdm import tqdm

def cos_sim(vec1, vec2):
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return -1
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def spearman_rank(rank1, rank2):
    if len(rank1) != len(rank2):
        return "check rank length!"
    N = len(rank1)
    D = sum((rank1 - rank2) ** 2)
    p = 1 - (6 * D)/(N ** 3 - N)
    return p

human_score = []
svd_score = []
word2vec_score = []

with open('section10/wordsim353/combined.tab', 'rt') as f:
    flag = True
    for line in tqdm(f.readlines()):
        if flag:
            flag = False
            continue
        line = line.split()
        score = line[2]
        human_score.append(score)

with open('section10/combined85.tab', 'rt') as f:
    for line in tqdm(f.readlines()):
        line = line.split()
        score = line[2]
        svd_score.append(score)

with open('section10/combined90.tab', 'rt') as f:
    for line in tqdm(f.readlines()):
        line = line.split()
        score = line[2]
        word2vec_score.append(score)

human_rank = np.argsort(human_score)
svd_rank = np.argsort(svd_score)
word2vec_rank = np.argsort(word2vec_score)

print(spearman_rank(human_rank, svd_rank))
print(spearman_rank(human_rank, word2vec_rank))