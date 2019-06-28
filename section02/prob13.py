#paste col1.txt col2.txt > col1_col2_test.txt
#diff col1_col2.txt col1_col2_test.txt

with open('col1.txt') as col1, open('col2.txt') as col2, open('col1_col2.txt', mode='w') as col1_col2:
    for text1, text2 in zip(col1, col2):
            text1 = text1.replace('\n', '')
            text2 = text2.replace('\n', '')
            col1_col2.write(text1 + "\t" + text2 + "\n")