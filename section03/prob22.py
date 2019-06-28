import gzip
import json
import re

def get_uk(name):
    doc_result = []
    with gzip.open(name, 'rt') as j:
        for data in j:
            dict_uk = json.loads(data)
            if "イギリス" in dict_uk["title"]:
                return dict_uk["text"]

doc_uk = get_uk(name='jawiki-country.json.gz').split('\n')
category = []
for doc_text in doc_uk:
    if 'Category' in doc_text:
        category.append(doc_text)

doc_cat = []

for cat in category:
    doc_cat.append(re.sub(r'\[|Category:|\|.*$|\]', '', cat))

print(doc_cat)