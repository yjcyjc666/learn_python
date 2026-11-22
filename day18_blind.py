f = open("day18_blind.txt","r",encoding="utf-8")
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
best_word = ""
best_count = 0
for word, num in counts.items():
    if num > best_count:
        best_count = num
        best_word = word
print(f"全文冠军词：{best_word},出现了 {best_count} 次")