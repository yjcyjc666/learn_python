sentence = input("请输入一段话")
sentence = sentence.replace(","," ")
words = sentence.split(" ")
print(words)
print(len(words))
count = 0
for word in words:
    count = count + 1
    print(f"第{count}个词：{word}")
    if word == "Python":
        print("关键词检测")