import gzip
import json

with gzip.open('jawiki-country.json.gz', 'rt') as j:
    for data in j:
        country = json.loads(data)
        if 'イギリス' in country['title']:
            print(country['text'])