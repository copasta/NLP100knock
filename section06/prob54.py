
from lxml import etree, objectify

tree = etree.parse("section6/nlp.txt.xml")
root = tree.getroot()
document = root.find('document')
sentences = document.find('sentences')
for sentence in sentences:
    tokens = sentence.find('tokens')
    for token in tokens:
        print('{}\t{}\t{}'.format(token.find('word').text,token.find('lemma').text,token.find('POS').text))
