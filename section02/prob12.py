#cut -f 1 hightemp.txt > col1_test.txt
#diff col1.txt col1_test.txt
#cut -f 2 hightemp.txt > col2_test.txt
#diff col2.txt col2_test.txt

with open('hightemp.txt') as f, open('col1.txt', mode='w') as col1, open('col2.txt', mode='w') as col2:
    for text in f:
        cols = text.split('\t')
        col1.write(cols[0] + '\n')
        col2.write(cols[1] + '\n')