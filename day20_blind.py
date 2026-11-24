f = open("day20_blind.txt","r",encoding="utf-8")
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
for letter,num in counts.items():
    if letter == "o":
        print(f"字母o:{letter},出现了{num}次")
