def read_file(name):
    try:
        f = open(name,"r",encoding="utf-8")
        text = f.read()
        f.close()
        text = text.replace(","," ").replace("."," ")
        return text
    except FileNotFoundError:
        return ""
def split_words(text):
    words = text.split()
    return words
def words_counts(words):
    num = (len(words))
    return num
def analyze(text):
    words = split_words(text)
    num = words_counts(words)
    return num
for name in ("day24_blind.txt", "no_exist.txt"):
    text = read_file(name)         
    if not text:                    
        print(f"跳过：{name} 不存在")
    else:
        print(f"{name}:{analyze(text)} 个词")   
