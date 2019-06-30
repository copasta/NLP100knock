from scipy import sparse, io
from sklearn.decomposition import TruncatedSVD

print('load matrix')
matrix = io.loadmat("section09/matrix")['mt']

print('decomposition')
svd = TruncatedSVD(n_components=300)
matrix_300 = svd.fit_transform(matrix)

print('save matrix')
io.savemat("section09/matrix_300", {"matrix":matrix_300})