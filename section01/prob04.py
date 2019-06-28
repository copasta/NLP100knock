def get_dict(s):
    s = s.replace('.', '').replace(',', '')
    word = s.split(' ')
    dic = {}
    for i in range(len(word)):
        if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            get_len = 2
        else:
            get_len = 1
        dic[word[i][:get_len]] = i+1
    return dic

if __name__ == "__main__":
    text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    print(get_dict(text))