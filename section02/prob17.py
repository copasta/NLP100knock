#cut -f 1 hightemp.txt |sort | uniq > result_test.txt
#python /Learning/NLP100knock/section2/prob17.py | sort > result.txt
#diff result.txt result_test.txt

with open('hightemp.txt') as f:
    l = set()
    for text in f:
        cols = text.split('\t')
        l.add(cols[0])

for i in l:
    print(i)