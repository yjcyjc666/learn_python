scores = {"灭霸": 95,"钢铁侠": 90,"Peter": 100}
print(scores["灭霸"])
print(scores["Peter"])
print(len(scores))
scores ["浩克"] = 88
scores ["灭霸"] = 99
print(scores)
print("浩克" in scores)
print("雷神" in scores)

counts = {}
words = ["灭霸","钢铁侠","灭霸","Peter","灭霸"]
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
print(counts)