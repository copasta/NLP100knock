from lxml import etree

def s_eq(sent):
    for idx, s in enumerate(sent):
        if s != 'NP':
            continue
        nest = 1
        word = []
        for i in range(idx + 1, len(sent)):
            if sent[i] == '(':
                nest += 1
            elif sent[i] == ')':
                nest -= 1
                if sent[i-1] != ')':
                    word.append(sent[i-1])
            if nest == 0:
                break
        if len(word) > 0:
            yield word

if __name__ == "__main__":
    tree = etree.parse("nlp.txt.xml")
    root = tree.getroot()
    doccument = root.find('document')
    sentences = doccument.find('sentences')
    for sentence in sentences:
        parse = sentence.find('parse')
        s = parse.text
        s = s.replace('(', ' ( ')
        s = s.replace(')', ' ) ')
        s = s.split(' ')
        for ss in s_eq(s):
            for sss in ss:
                if len(sss) != 0:
                    print(sss)