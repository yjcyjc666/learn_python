price = float(input("请输入订单金额"))
if price >= 100:
    print("100减20红包")
    red_packet = 20
elif price >= 60:
    print("60减10红包")
    red_packet = 10
elif price >= 30:
    print("30减5红包")
    red_packet = 5
else:
    print("无红包")
    red_packet = 0
delivery_fee = float(input("请输入配送费"))
member_per_order = round(price-red_packet,2)
not_member_per_order = round(price-red_packet+delivery_fee,2)
member = input("是否是会员？(yes/no)")
if member == "yes":
    print("无配送费结算")
    print(f"本单实际支付:{member_per_order}")
else:
    print("有配送费结算")
    print(f"本单实际支付:{not_member_per_order}")