pens = int(input()) * 5.8
markers = int(input()) * 7.2
cleaner = float(input()) * 1.2
percent_discount = int(input())

all_supply_price = pens + markers + cleaner
discount = all_supply_price - ((all_supply_price * percent_discount) / 100)
print(f"{discount:.3f}")