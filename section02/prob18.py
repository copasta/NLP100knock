#sort hightemp.txt -k 3 -r  > result_test18.txt
#diff result_18.txt result_test18.txt

import pandas as pd

hightemp = pd.read_table('hightemp.txt', header=None)
hightemp_ = hightemp.sort_values(2, ascending=False).reset_index(drop=True)
hightemp_.to_csv('result_18.txt', header=False, index=False, sep='\t')