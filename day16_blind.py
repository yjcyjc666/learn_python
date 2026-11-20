f = open(input("请输入文件"),"r",encoding="utf-8")
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
top1 = sorted(counts.items(),key=lambda x:x[1],reverse=True)[:1]
print(top1)
once_counts = 0
for word,num in counts.items():
    if num == 1:
        once_counts += 1
print(f"只出现一次的单词有{once_counts}个")