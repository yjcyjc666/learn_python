f = open("day19_blind.txt","r",encoding="utf-8")
text = f.read()
f.close()
text = text.replace(","," ").replace("."," ").replace(":"," ")
words = text.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
print(counts)
best = 0
for word,num in counts.items():
    if num > best:
        best = num
champs = []
for word,num in counts.items():
    if num == best:
        champs.append(word)
print(f"出现最多的词有：{len(champs)},出现了{best}次")
for word in champs:
    print(word)