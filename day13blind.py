import jieba
jieba.add_word("小美")
jieba.add_word("狗")
jieba.add_word("大黄")
jieba.add_word("煤球")
f = open(input("请输入文件名"),"r",encoding="utf-8")
text = f.read()
f.close()
words = jieba.lcut(text)
print(words)
clean_words = []
stopwords = ["了","一","只","再","就","和","除","见","和","什么","都","是","可","还","的"]
for word in words:
    if word == "\n":
        continue
    if word in stopwords:
        continue
    if word in " ，。：；“”‘’？！【】（） ":
        continue
    clean_words.append(word)
print(clean_words)
count = {}
for word in clean_words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1
print(count)
top3 = sorted(count.items(),key=lambda x:x[1],reverse=True)[:3]
print(top3)
for word, num in top3:
    print(f"{word} 出现了 {num} 次")
