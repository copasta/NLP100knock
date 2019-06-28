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

basic_info = {}

for text in doc_uk:
    if ' = ' in text:
        text = text[1:].split(' = ')
        text[1] = re.sub('\'+?','',text[1])
        if 'ファイル' not in text[1]:
            text[1] = re.sub('\[+?', '', text[1])
            text[1] = re.sub('\]+?', '', text[1])
        basic_info[text[0]] = text[1]

# https://www.mediawiki.org/wiki/API:Imageinfo
import urllib.request
url = basic_info['国旗画像']
url = "https://commons.wikimedia.org/w/api.php?action=query&titles=File:{}&prop=imageinfo&iiprop=url&format=json".format(url)
url = url.replace(" ", "+")
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode("utf-8"))
pages = data["query"]["pages"]
for k in pages.keys():
    if "imageinfo" in pages[k].keys():
        print(pages[k]["imageinfo"][0]["url"])
