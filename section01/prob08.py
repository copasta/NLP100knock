def cipher(s):
    t = []
    for i in s:
        n = ord(i)
        if n >= ord('a') and n <= ord('z'):
            t.append(chr(219 - n))
        else:
            t.append(i)
    return "".join(t)

if __name__ == "__main__":
    text = "I am an NLPer."
    print('original  :{}'.format(text))
    print('encryption:{}'.format(cipher(text)))
    print('decryption:{}'.format(cipher(cipher(text))))