
import gzip
import leveldb
import json

db = leveldb.LevelDB('/Learning/NLP100knock/section7/music_list.ldb')

with gzip.open('artist.json.gz') as f:
    for line in f:
        jdata = json.loads(line)

        try:
            name = jdata['name']
            tags = json.dumps(jdata['tags'])
            db.Put(name.encode('utf-8'), tags.encode('utf-8'))
        except KeyError:
            pass
