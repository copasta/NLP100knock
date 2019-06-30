from lxml import etree

## 参考 https://python.keicode.com/advanced/xml-lxml-1.php

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()

for word in root.findall(".//word"):
    print(word.text)