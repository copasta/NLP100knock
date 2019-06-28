def n_gram(s, n, u='word'):
    s = s.replace('.', '').replace(',', '')
    s = s.split(' ')
    if u == 'char':
        s_ = []
        for i in s:
            for j in i:
                s_.append(j)
        s = s_
    t = []
    for i in range(len(s)):
        if i+n-1 < len(s):
            t.append("".join(s[i:i+n]))
    return t

if __name__ == "__main__":
    s1 = 'paraparaparadise'
    s2 = 'paragraph'

    X = set(n_gram(s1, 2, u='char'))
    Y = set(n_gram(s2, 2, u='char'))

    print("Union          :{}".format(X|Y))
    print("Intersection   :{}".format(X&Y))
    print("Difference(X-Y):{}".format(X-Y))
    print("Difference(Y-X):{}".format(Y-X))

    print("Is \'se\' in X?:{}".format('se' in X))
    print("Is \'se\' in Y?:{}".format('se' in Y))