# Stanford Core NLP

1. ダウンロード  
2. 下記のコマンドでxmlファイルを作成  
```
java -cp "*" -Xmx3g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt
```
  