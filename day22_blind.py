def read_file(filename):
    f = open(filename,"r",encoding="utf-8")
    text = f.read()
    f.close()
    return text
def text_split(text):
    text = text.replace(","," ").replace("."," ")
    words = text.split()
    return words
def find_longest(words):
    longest = "" 
    letter = 0
    for word in words:
        if len(word) > letter:
            letter = (len(word))
            longest = word
    return longest, letter
text = read_file("day17_blind.txt")
split = text_split(text)   
result = find_longest(split)
print(f"最长词：{result[0]},有字母{result[1]}个")