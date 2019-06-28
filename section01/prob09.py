import random
def typoglycemia(s, seed):
    s = s.split(' ')
    t = []
    for word in s:
        if len(word) > 4:
            word_len = len(word)
            shuffle_word = [c for c in word[1:word_len-1]]
            random.seed(seed)
            random.shuffle(shuffle_word)
            t.append(word[0]+"".join(shuffle_word)+word[word_len-1])
            t.append(' ')
        else:
            t.append(word)
            t.append(' ')
    return "".join(t)

if __name__ == "__main__":
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(text)
    print(typoglycemia(text, seed=1234))