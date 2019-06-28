
#cut -f 1 hightemp.txt | sort | uniq -c | sort -r

import pandas as pd

hightemp = pd.read_table('hightemp.txt', header=None)
print(hightemp[0].value_counts())