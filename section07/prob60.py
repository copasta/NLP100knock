
## plyvelはだめ．
## インストールで手こずった挙句 image not foundが帰って来た

import gzip
import leveldb
import json

db = leveldb.LevelDB('/Learning/NLP100knock/section7/music_list.ldb')

with gzip.open('artist.json.gz') as f:
    for line in f:
        jdata = json.loads(line)

        try:
            name = jdata['name']
            area = jdata['area']
            db.Put(name.encode('utf-8'), area.encode('utf-8'))
        except KeyError:
            pass
print('{}件登録しました。'.format(len(list(db.RangeIter(include_value=False)))))
