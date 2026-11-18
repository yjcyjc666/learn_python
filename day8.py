count = 1
while count <= 5:
    print(f"这是第{count}次循环")
    count = count+1
total = 0
i = 1
while i <= 100:
    total = total+i
    i = i+1
print(f"1加到100的总和是:{total}")
while True:
    password = input("请输入密码") 
    if password == "1234":
        print("登陆成功")
        break
    print("密码错误，再试一次")
print("程序结束")