import gzip
import json
import re
import collections

def get_uk(name):
    doc_result = []
    with gzip.open(name, 'rt') as j:
        for data in j:
            dict_uk = json.loads(data)
            if "イギリス" in dict_uk["title"]:
                return dict_uk["text"]

doc_uk = get_uk(name='jawiki-country.json.gz').split('\n')

section = {}

for text in doc_uk:
    if '==' in text:
        section[re.sub('=| ', '', text)] = int(text.count('=')/2 -1)

print(section)