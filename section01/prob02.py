def str_cat(s1, s2):
    ln = len(s1) if len(s1) < len(s2) else len(s2)
    ans = []
    for i in range(ln):
        ans.append(s1[i])
        ans.append(s2[i])
    ans.append(s1[ln:])
    ans.append(s2[ln:])
    return ''.join(ans)

if __name__ == "__main__":
    s1 = 'パトカー'
    s2 = 'タクシー'
    print(str_cat(s1, s2))