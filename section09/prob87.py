import pickle
from scipy import io, sparse
import numpy as np

def cos_sim(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

with open('section09/matrix_key', 'rb') as f:
    keys = pickle.load(f)

matrix_300 = io.loadmat("section09/matrix_300")['matrix']

vec_united_state = matrix_300[keys['United_States']]
vec_us = matrix_300[keys['U.S']]

print(cos_sim(vec_united_state, vec_us))
