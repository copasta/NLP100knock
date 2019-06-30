from collections import defaultdict
import pickle
from tqdm import tqdm

co_t_c = defaultdict(int)
em_t = defaultdict(int)
em_c = defaultdict(int)
N = 0

with open("section09/context.txt", "rt") as f:
    for line in tqdm(f.readlines()):
        words = line.split("\t")
        t = words[0]
        em_t[t] += 1
        for c in words[1].strip().split():
            em_c[c] += 1
            co_t_c[(t, c)] += 1
            N += 1

pickle.dump(co_t_c, open("section09/context_t_c", 'wb'))
pickle.dump(em_t, open("section09/count_t", 'wb'))
pickle.dump(em_c, open("section09/count_c", 'wb'))
print(N)