#split -l 5 hightemp.txt
#

N = int(input('N:'))
with open('hightemp.txt') as f:
    text = f.readlines()

    num_rows = len(text)
    p = num_rows // N
    q = num_rows % N
    c = 0
    
    for i in range(N):
        s = i * p + c
        if q > 0:
            c+=1
            q-=1
        e = i * p + p + c
        if e > num_rows and i == N-1:
            e = num_rows
        print("n={}".format(i+1))
        for t in text[s:e]:
            print(t)
