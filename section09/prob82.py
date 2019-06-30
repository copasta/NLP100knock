import random
from tqdm import tqdm

with open("section09/corpus81.txt", 'rt') as f, open("section09/context.txt", "wt") as g:
    for line in tqdm(f.readlines()):
        line = line.replace("\n", "")
        line = line.split()
        for idx in range(len(line)):
            t = line[idx]
            d = random.randint(1, 6)
            temp = []
            for k in range(max(idx - d, 0), min(idx + d + 1, len(line))):
                if idx != k:
                    temp.append(line[k])
            
            if len(temp) != 0:
                #print("{}\t".format(line[idx]),end="")
                #print(" ".join(temp))
                g.write(line[idx])
                g.write("\t")
                g.write(" ".join(temp))
                g.write("\n")
            else:
                #print("{}\t{}".format(line[idx], "N/A"))
                g.write(line[idx])
                g.write("\t")
                g.write("N/A\n")