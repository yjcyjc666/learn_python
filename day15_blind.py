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
print(counts)
print(f"不同的词有{len(counts)}个")
top1 = sorted(counts.items(),key=lambda x:x[1],reverse=True)[:1]
print(top1)
for word, num in top1:
    print(f"{word}一共出现了{num}次")