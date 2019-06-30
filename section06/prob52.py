import re
from stemming.porter2 import stem

def generate():
    doc_nlp = []
    with open('section6/nlp.txt') as f:
        for line in f.readlines():
            sline = re.split(r'(^.*?[!\?\.:;])(\s)([A-Z].*)', line)
            for ss in sline:
                if '\n' in ss:
                    ss = re.sub('\n', '', ss)
                if len(ss) == 0 or ss == ' ':
                    continue
                doc_nlp.append(ss)
    return doc_nlp


if __name__ == "__main__":
    doc_nlp = generate()
    for doc in doc_nlp:
        doc = doc.replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('\"', '')
        doc = doc.split(' ')
        for word in doc:
            print('{}\t{}'.format(word,stem(word)))
        print()
