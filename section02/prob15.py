#tail -n 2 hightemp.txt

N = int(input('N:'))
with open('hightemp.txt') as f:
    text = f.readlines()
    for c in text[max(len(text)-N, 0):]:
        print(c, end='')