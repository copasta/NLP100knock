#expand -t 1 hightemp.txt

def tab_to_space(f):
    t = []
    for c in f:
        t.append(c.replace("\t", " "))
    return t

with open('hightemp.txt') as f:
    ans = tab_to_space(f)
    for text in ans:
        print(text, end='')