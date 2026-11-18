total = 0
count = 0
while True:
    cash_register = float(input("请输入金额："))
    if cash_register == 0:
        print("收银结束")
        break
    if cash_register < 0:
        print("本轮跳过")
        continue
    print("收银成功")
    total = total + cash_register
    count = count + 1
print(f"今日收银次数：{count}")
print(f"今日收银总数：{round(total,2)}元")