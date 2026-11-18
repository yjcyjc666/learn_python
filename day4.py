price = 32.5
red_packet = 5
monthly_count = 12
delivery_fee = 3
per_order = price-red_packet+delivery_fee
monthly_total = round(per_order*monthly_count,2)
print(f"这一单实际支付：{per_order}")
print(f"本月总支出：{monthly_total}")