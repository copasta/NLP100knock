
import pymongo
from pymongo import MongoClient

client = MongoClient()
## データベースの作成
db = client.NLP100knock 
## コレクションの取得
collection = db.artist

name = 'スマップ'
data = collection.find({'tags.value':'dance'})
data = data.sort('rating.count', pymongo.DESCENDING)

count = 0
for doc in data:
    print(doc)
    count += 1
    if count == 10:
        break


