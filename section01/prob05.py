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
    text = 'I am an NLPer'
    print(n_gram(text, 2, 'word'))
    print(n_gram(text, 2, 'char'))