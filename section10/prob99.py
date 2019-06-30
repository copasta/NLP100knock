import pickle
import numpy as np
from scipy import io
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

with open('section10/country_to_id', 'rb') as f:
    country_to_id = pickle.load(f)
matrix = io.loadmat("section10/country_matrix")["matrix"]

model = TSNE()
visualized_vec = model.fit_transform(matrix)

plt.figure(figsize=(20,20))
fig, ax = plt.subplots()
for index, country in enumerate(country_to_id.keys()):
    ax.scatter(visualized_vec[index, 0], visualized_vec[index, 1], marker='.')
    ax.annotate(country, xy=(visualized_vec[index, 0], visualized_vec[index, 1]))
plt.tight_layout()
plt.savefig("section10/country_tsne.png")