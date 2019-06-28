#wc -l hightemp.txt <-23
#awk 'END{print NR}' hightemp.txt <-24

with open('hightemp.txt') as f:
    temp = f.readlines()
    print(len(temp))