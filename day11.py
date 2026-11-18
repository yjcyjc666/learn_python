f = open("article.txt","r",encoding = "utf-8")
text = f.read()
f.close()
print(len(text))
text = text.replace("，"," ").replace(","," ")
words = text.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
print(f"全文共计 {len(words)} ,其中不同的词有 {len(counts)} 个")
best_word = ""
best_counts = 0
for word, num in counts.items():
    if num > best_counts:
        best_counts = num
        best_word = word
print(f"全文冠军词：{best_word},出现了 {best_counts} 次")
ranking = sorted(counts.items(),key=lambda x:x[1],reverse=True)
for word,num in ranking[:5]:
    print(f"{word}:{num}")
print(words)
print(counts)
