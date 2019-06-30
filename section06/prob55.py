
from lxml import etree, objectify

tree = etree.parse("section6/nlp.txt.xml")
root = tree.getroot()
document = root.find('document')
sentences = document.find('sentences')
for sentence in sentences:
    tokens = sentence.find('tokens')
    for token in tokens:
        word = token.find('word').text
        ner = token.find('NER').text
        if ner == 'PERSON':
            print(word)
