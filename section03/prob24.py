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

doc_uk = get_uk(name='section3/jawiki-country.json.gz').split('\n')

for text in doc_uk:
    med_file = re.findall(r'(?:File|ファイル):(.+?)\|', text)
    if len(med_file) > 0:
        print(med_file)