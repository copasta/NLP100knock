import pickle
import numpy as np
from scipy import io
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from matplotlib import pyplot as plt

with open('section10/country_to_id', 'rb') as f:
    country_to_id = pickle.load(f)
matrix = io.loadmat("section10/country_matrix")["matrix"]

pred = linkage(matrix, method='ward')
country = list(country_to_id)

plt.figure(figsize=(14,7))
dendrogram(pred, labels=country, leaf_font_size=7)
print("save denogram")
plt.tight_layout()
plt.savefig("section10/country_denogram.png")