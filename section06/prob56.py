
from lxml import etree, objectify

## 難しい 参考 https://qiita.com/segavvy/items/0340d3d71c9151265bcb

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()
document = root.find('document')
sentences = document.find('sentences')

rep_dict = {}

for coreference in document.find('coreference'):
    rep_text = coreference.findtext('./mention[@representative="true"]/text')
    for mention in coreference.findall('mention'):
        if mention.get('representative', 'false') == 'false':

            sent_id = int(mention.findtext('sentence'))
            start = int(mention.findtext('start'))
            end = int(mention.findtext('end'))

            if not (sent_id, start) in rep_dict:
                rep_dict[(sent_id, start)] = (end, rep_text)
        
for sentence in sentences:
    sent_id = int(sentence.get('id'))
    org_rest = 0

    for token in sentence.find('tokens'):
        token_id = int(token.get('id'))

        if org_rest == 0 and (sent_id, token_id) in rep_dict:
            end, rep_text = rep_dict[(sent_id, token_id)]

            print('[{}]('.format(rep_text), end='')
            org_rest = end - token_id
        
        print(token.findtext('word'), end='')

        if org_rest > 0:
            org_rest -= 1
            if org_rest == 0:
                print(')', end='')
            
        print(' ', end='')
    print