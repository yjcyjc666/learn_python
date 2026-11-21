f = open("day17_blind.txt","r",encoding="utf-8")
text = f.read()
f.close()
text = text.replace(","," ").replace("."," ")
words = text.split()
longest_words = "" 
letter = 0
for word in words:
    if len(word) > letter:
        letter = (len(word))
        longest_words = word
print(f"最长词：{longest_words},有字母{letter} 个")   
