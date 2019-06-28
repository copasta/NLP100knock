import MeCab

with open('neko.txt') as input_file, open('neko.txt.mecab', 'w') as output_file:
    mecab = MeCab.Tagger()
    output_file.write(mecab.parse(input_file.read()))