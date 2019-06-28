
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
    AnoB = []
    for i, neko in enumerate(waganeko):
        if i == len(waganeko) - 1:
            break
        if neko['surface'] == 'の':
            if waganeko[i-1]['pos'] == '名詞' and waganeko[i+1]['pos'] == '名詞':
                AnoB.append(''.join(waganeko[i-1]['surface'] + neko['surface'] + waganeko[i+1]['surface']))
    print(set(AnoB))