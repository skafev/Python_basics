Lily_age = int(input())
price_for_washer = float(input())
price_for_toy = int(input())
budget = 0
new_budget = 0
toys = 0
money_from_toys = 0
for n in range(1, Lily_age + 1):
    if n % 2 == 0:
        budget += 10
        new_budget = new_budget + budget - 1
    else:
        toys += 1
money_from_toys = toys * price_for_toy
new_budget += money_from_toys
if new_budget >= price_for_washer:
    print(f"Yes! {new_budget - price_for_washer:.2f}")
else:
    print(f"No! {price_for_washer - new_budget:.2f}")

