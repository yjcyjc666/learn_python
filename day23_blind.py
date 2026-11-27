def read_file(name):
    f = open(name,"r",encoding="utf-8")
    text = f.read()
    f.close()
    return text
def clean_words(text):
    text = text.replace(","," ").replace("."," ")
    return text
def word_num(words):
    words = words.split()
    return len(words)
text = read_file("day23_blind.txt")
words = clean_words(text)
result = word_num(words)
print(f"文本：{words}")
print(f"全文共计{result}个词")