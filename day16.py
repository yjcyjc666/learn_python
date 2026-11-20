import jieba
jieba.add_word("灭建国")
jieba.add_word("灭国栋")
jieba.add_word("灭富贵")
jieba.add_word("灭狗剩")
jieba.add_word("灭小看")
jieba.add_word("灭狗蛋")
jieba.add_word("灭彩霞")
jieba.add_word("灭莲花")
def read_file(filename):    
    f = open(filename,"r",encoding = "utf-8")
    text = f.read ()
    f.close ()
    return text
stopwords = ["的","了","是","在","和","不","有","也","这","那"]
def clean_words_list(words):
    clean_words = []
    for word in words:
        if word == "\n":
            continue
        if word in stopwords:
            continue
        if word in "，。；：""''（）——":
            continue
        clean_words.append(word)
    return clean_words
def counts_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts
def print_top(counts, n):
    top = sorted(counts.items(),key=lambda x:x[1],reverse=True)[:n]
    for word,num in top:
        print(f"{word}出现了{num}次")
text = read_file("article_cn.txt")
words = jieba.lcut(text)
clean = clean_words_list(words)
counts = counts_words(clean)
print_top(counts,10)