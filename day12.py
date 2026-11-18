import jieba
jieba.add_word("灭建国")
jieba.add_word("灭国栋")
jieba.add_word("灭富贵")
jieba.add_word("灭狗剩")
jieba.add_word("灭小看")
jieba.add_word("灭狗蛋")
jieba.add_word("灭彩霞")
jieba.add_word("灭莲花")
f = open("article_cn.txt","r",encoding = "utf-8")
text = f.read ()
f.close ()
words = jieba.lcut(text)
stopwords = ["的","了","是","在","和","不","有","也","这","那"]
clean_words = []
for word in words:
    if word == "\n":
        continue
    if word in stopwords:
        continue
    if word in "，。；：""''（）——":
        continue
    clean_words.append(word)
print(clean_words)
counts = {}
for word in clean_words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
top10 = sorted (counts.items(),key=lambda x:x[1],reverse=True)[:10]
print(top10)
for word,num in top10:
    print(f"{word}出现了{num}次")