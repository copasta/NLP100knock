from tqdm import tqdm
with open('section10/family90.txt', 'rt') as f:
    cnt = 0
    total = 0
    for line in tqdm(f.readlines()):
        line = line.split()
        if line[3] == line[4]:
            cnt += 1
        total += 1
    print(cnt*100/total)

with open('section10/family85.txt', 'rt') as f:
    cnt = 0
    total = 0
    for line in tqdm(f.readlines()):
        line = line.split()
        if line[3] == line[4]:
            cnt += 1
        total += 1
    print(cnt*100/total)