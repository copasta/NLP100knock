import re

def generate():
    doc_nlp = []
    with open('nlp.txt') as f:
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
        print(doc)
