import bz2
from tqdm import tqdm

c = 0
with bz2.open("section09/enwiki-20150112-400-r100-10576.txt.bz2", "rt") as f, open("section09/corpus.txt", mode='wt') as g:
    for line in tqdm(f.readlines()):
        line = line.split()
        for idx in range(len(line)):
            line[idx] = line[idx].strip(".,!?;:()[]\'\"")
        if len(line) == 0:
            continue
        g.write(" ".join(line))
        g.write("\n")