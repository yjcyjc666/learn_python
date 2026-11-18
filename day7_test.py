price = float(input("请输入金额"))
if price >= 100:
    print("100减20红包")
    red_packet = 20
elif price >= 60:
    print("60减10红包")
    red_packet = 10
elif price >= 40:
    print("40减5红包")
    red_packet = 5
else:
    print("无红包")
    red_packet = 0
per_order = round(price-red_packet,2)
delivery_fee = float(input("请输入配送费"))
member = input("是否为会员?(yes/no)")
if member == "yes":
    print("会员无配送费结算")
    total_spend = round(per_order,2)
    print(f"总金额:{total_spend}")
else:
    print("非会员结算")
    total_spend = round(per_order+delivery_fee,2)
    print(f"总金额:{total_spend}")