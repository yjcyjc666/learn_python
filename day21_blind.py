f = open("day21_blind.txt","r",encoding="utf-8")
text = f.read()
f.close()
text = text.replace(","," ").replace("."," ")
words = text.split()
counts = {}
for word in words:
    for letter in word:
        if letter in counts:
            counts[letter] = counts[letter] + 1
        else:
            counts[letter] = 1
for v in "aeiou":
    print(f"字母{v}出现了{counts.get(v, 0)}次")
