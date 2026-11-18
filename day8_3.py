for i in range (1,6):
    print(f"第{i}圈")
fruits = ["苹果","香蕉","橘子"]
for fruits in fruits:
    print(f"今天吃{fruits}")
total = 0
for i in range (1,101):
    if i % 2 == 0:
        total = total + i
print(total)

total2=0
for i in range (2, 102, 2):
    total2 = total2 + i
print(total2)