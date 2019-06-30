from gensim.models import word2vec, KeyedVectors
import numpy as np
import pickle

def cos_sim(vec1, vec2):
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return -1
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


'''
print('word2vec')
data = word2vec.Text8Corpus("section09/corpus81.txt")
model = word2vec.Word2Vec(data, size=300)
model.wv.save_word2vec_format('section10/matrix_word2vec.txt', binary=True)
'''

model = KeyedVectors.load_word2vec_format('section10/matrix_word2vec.txt', binary=True)

print('prob86')
print(model['United_States'])

print('prob87')
print(cos_sim(model['United_States'], model['U.S']))

print('prob88')
for result in model.most_similar(u'England', topn=10):
    print(result)

print('prob89')
for result in model.most_similar(positive=[u'England',u'Athens'], negative=[u'Madrid'], topn=10):
    print(result)