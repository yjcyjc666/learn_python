import jieba
jieba.add_word("威震天")
jieba.add_word("御天敌")
f = open(input("请输入文件名"),"r",encoding="utf-8")
text = f.read()
f.close()
text = text.replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ")
words = jieba.lcut(text)
stopwords = ["里","了","被","一次","还"]
clean_words = []
for word in words:
    if word == "\n":
        continue
    if word in "，。？！”“‘’；：【】—— ":
        continue
    if word in stopwords:
        continue
    clean_words.append(word)
print(clean_words)
counts = {}
for word in clean_words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
top10 = sorted(counts.items(),key=lambda x:x[1],reverse=True)[:10]
print(top10)