f = open(input("请输入文件名"),"r",encoding="utf-8")
text = f.read()
f.close()
text = text.replace(","," ").replace("."," ")
words = text.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
top3 = sorted(counts.items(),key=lambda x:x[1],reverse=True)[:3]
print(top3)
for word, num in top3:
    print(f"{word}出现了{num}次")