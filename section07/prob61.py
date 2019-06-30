
import leveldb

db = leveldb.LevelDB('/Learning/NLP100knock/section7/music_list.ldb')

print(db.Get('カントリー娘。に紺野と藤本（モーニング娘。）'.encode('utf-8')).decode('utf-8'))