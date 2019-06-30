

import gzip
import pymongo
from pymongo import MongoClient
import json

client = MongoClient()
## データベースの作成
db = client.NLP100knock 
## コレクションの取得
collection = db.artist

with gzip.open('artist.json.gz', 'rt') as f:
    buf = []
    for i, line in enumerate(f, 1):
        jdata = json.loads(line)
        buf.append(jdata)
    collection.insert_many(buf)

collection.create_index([('name', pymongo.ASCENDING)])  
collection.create_index([('aliases.name', pymongo.ASCENDING)])  
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])