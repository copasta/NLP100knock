from collections import Counter
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'IPAexGothic'
plt.style.use('ggplot')

def get_nekodic():
    nekodic = []
    dic = {}
    with open('section04/neko.txt.mecab') as f:
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
    word_c = Counter()
    word_c.update([neko['surface'] for neko in waganeko])
    result_c = word_c.most_common(10)
    label = []
    count = []
    for i in result_c:
        label.append(i[0])
        count.append(i[1])
    plt.bar(label, count)
    plt.show()