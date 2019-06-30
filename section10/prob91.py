
with open('section10/questions-words.txt', 'rt') as f, open('section10/family.txt', 'wt') as g:
    flag = False
    for line in f.readlines():
        if flag:
            if line.startswith(":"):
                break
            g.write(line)
                
        if line.startswith(": family"):
            flag = True