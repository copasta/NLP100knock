
def get_nekodic():
    nekodic = []
    dic = {}
    with open('neko.txt.mecab') as f:
        for line in f.readlines():
            line = line[:-1]
            line = line.split('\t')
            if len(line) < 2:
                break
            surface = line[0]
            res = line[1].split(',')
            dic = {
                'surface': surface,
                'base': res[6],
                'pos': res[0],
                'pos1': res[1]
            }
            nekodic.append(dic)
    return nekodic

if __name__ == "__main__":
    waganeko = get_nekodic()
    neko_verb = []
    for neko in waganeko:
        if neko['pos'] == '動詞':
            neko_verb.append(neko['surface'])
    print(neko_verb)