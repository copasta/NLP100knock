import pickle
from scipy import io, sparse

with open('section09/matrix_key', 'rb') as f:
    keys = pickle.load(f)

matrix_300 = io.loadmat("section09/matrix_300")['matrix']

print(matrix_300[keys['United_States']])