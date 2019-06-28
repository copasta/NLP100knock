from collections import Counter
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'IPAexGothic'
plt.style.use('ggplot')

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
    word_c = Counter()
    word_c.update([neko['surface'] for neko in waganeko])
    result_c = word_c.most_common()
    rank = []
    count = []
    for i, j in enumerate(result_c):
        rank.append(i+1)
        count.append(j[1])
    plt.scatter(rank, count)
    plt.xlabel('出現頻度順位')
    plt.ylabel('出現頻度')
    plt.xlim(1, len(rank) + 1)
    plt.ylim(1, max(count))
    plt.xscale('log')
    plt.yscale('log')
    plt.show()