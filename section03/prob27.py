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

basic_info = {}

for text in doc_uk:
    if ' = ' in text:
        text = text[1:].split(' = ')
        text[1] = re.sub('\'+?','',text[1])
        if 'ファイル' not in text[1]:
            text[1] = re.sub('\[+?', '', text[1])
            text[1] = re.sub('\]+?', '', text[1])
        basic_info[text[0]] = text[1]

for k, v in basic_info.items():
    print("{}:{}".format(k, v))