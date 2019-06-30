
# # db.artist.find({name:'Queen'})

import pymongo
from pymongo import MongoClient

client = MongoClient()
## データベースの作成
db = client.NLP100knock 
## コレクションの取得
collection = db.artist

for data in collection.find({'name': 'Queen'}):
    print (data)