import pickle
from scipy import io, sparse
import numpy as np

def cos_sim(vec1, vec2):
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return -1
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

with open('section09/matrix_key', 'rb') as f:
    keys = pickle.load(f)

matrix_300 = io.loadmat("section09/matrix_300")['matrix']

vec_England = matrix_300[keys['England']]

sim_dic = {}

for key, value in keys.items():
    if key != 'England':
        sim_dic[key] = cos_sim(vec_England, matrix_300[value])

sim_dic = sorted(sim_dic.items(), key=lambda x:x[1], reverse=True)

for key, value in sim_dic[:10]:
    print("{}:{}".format(key, value))
