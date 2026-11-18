price = float(input("请输入金额"))
if price < 30:
    print("无红包")
    red_packet = 0
elif 30 < price <= 60:
    print("30减5红包")
    red_packet = 5
elif  60 < price <= 100:
    print("60减10红包")
    red_packet = 10
else:
    print("100减20红包")
    red_packet = 20