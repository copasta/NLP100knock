import pickle
from collections import defaultdict, OrderedDict
from scipy import sparse, io
from math import log
from tqdm import tqdm

N = 79004342

def generate_context_matrix(co_t_c, em_t, em_c):
    t_word_to_id = OrderedDict((key, i) for i, key in enumerate(em_t.keys()))
    c_word_to_id = OrderedDict((key, i) for i, key in enumerate(em_c.keys()))
    matrix = sparse.lil_matrix((len(t_word_to_id), len(c_word_to_id)))
    
    for k, v in tqdm(co_t_c.items()):
        if v >= 10:
            #print(k)
            t = k[0]
            c = k[1]
            pmi = max(0, log((N*v)/(em_t[t]*em_c[c])))
            matrix[(t_word_to_id[t], c_word_to_id[c])] = pmi
    return t_word_to_id, matrix


co_t_c = pickle.load(open("section09/context_t_c", 'rb'))
em_t = pickle.load(open("section09/count_t", 'rb'))
em_c = pickle.load(open("section09/count_c", 'rb'))

keys, matrix = generate_context_matrix(co_t_c, em_t, em_c)

io.savemat("section09/matrix", {"mt":matrix})
with open("section09/matrix_key", "wb") as f:
    pickle.dump(keys, f)

