sentence = input("请输入一段话")
sentence = sentence.replace(","," ")
words = sentence.split()
counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
print(counts)
for word,num in counts.items():
    print(f"{word}出现了{num}次")