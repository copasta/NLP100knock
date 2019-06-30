from sklearn.cluster import KMeans
import pickle
import numpy as np
from scipy import io

with open('section10/country_to_id', 'rb') as f:
    country_to_id = pickle.load(f)
matrix = io.loadmat("section10/country_matrix")["matrix"]

model = KMeans(n_clusters=5)
pred = model.fit_predict(matrix)

for country, category in zip(country_to_id.keys(), pred):
    print("{} {}".format(country, category))