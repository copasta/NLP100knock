def get_word_len(s):
    s = s.replace('.', '').replace(',', '')
    word = s.split(' ')
    word_len = [len(w) for w in word]
    return word_len

if __name__ == "__main__":
    text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    print(get_word_len(text))