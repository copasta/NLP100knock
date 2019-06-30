
import leveldb

db = leveldb.LevelDB('/Learning/NLP100knock/section7/music_list.ldb')

count = 0

for k, v in db.RangeIter():
    if v == 'Japan'.encode('utf-8'):
        count += 1

print(count)