import jieba
jieba.add_word("灭建国")
jieba.add_word("灭国栋")
jieba.add_word("灭富贵")
jieba.add_word("灭狗剩")
jieba.add_word("灭小看")
jieba.add_word("灭狗蛋")
jieba.add_word("灭彩霞")
jieba.add_word("灭莲花")
jieba.add_word("威震天")
jieba.add_word("御天敌")
stopwords = ["的","了","是","在","和","不","有","也","这","那","里","一次"," ","还"]
class WordCounter:
    def __init__(self):
        self.total = 0
    def read_file(self,filename):    
        f = open(filename,"r",encoding = "utf-8")
        text = f.read ()
        f.close ()
        text = text.replace("2"," ").replace("3"," ").replace("4"," ").replace("5"," ")
        return text
    def clean_words_list(self,words):
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
    def counts_words(self,words):
        counts = {}
        for word in words:
            if word in counts:
                counts[word] = counts[word] + 1
            else:
                counts[word] = 1
        return counts
    def print_top(self,counts, n):
        top = sorted(counts.items(),key=lambda x:x[1],reverse=True)[:n]
        for word,num in top:
            print(f"{word}出现了{num}次")
    def analyze(self,filename):
        
        text = self.read_file(filename)
        words = jieba.lcut(text)
        clean = self.clean_words_list(words)
        counts = self.counts_words(clean)
        self.print_top(counts,5)
        self.total += 1
        return counts
files = ["article_day13.txt","article_none.txt","article_cn.txt","article_gbk.txt"]
results = {}
counter = WordCounter()
for name in files:
    try:
        results[name] = counter.analyze(name)
    except FileNotFoundError:
        print(f"{name}不存在，已跳过")
    except UnicodeDecodeError:
        print(f"{name}非utf-8编码,无法读取,已跳过")
import json
print(f"本次成功分析{counter.total}个文件")
with open("results.json","w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
with open("results.json","r",encoding="utf-8") as f:
    back = json.load(f)
print(f"读回 == 结果：{back == results}")