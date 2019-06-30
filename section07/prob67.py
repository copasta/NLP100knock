
import pymongo
from pymongo import MongoClient

client = MongoClient()
## データベースの作成
db = client.NLP100knock 
## コレクションの取得
collection = db.artist

name = 'スマップ'
data = collection.find({'aliases.name':name})

for doc in data:
    print(doc)