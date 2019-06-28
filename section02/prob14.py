#head -n 2 hightemp.txt

N = int(input('N:'))
with open('hightemp.txt') as f:
    text = f.readlines()
    for c in text[:min(len(text), N)]:
        print(c, end='')