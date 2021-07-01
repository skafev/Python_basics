flower_type = input()
flower_count = int(input())
budget = int(input())
price = 0
total_cost = 0

if flower_type == "Roses":
    price = 5
    total_cost = flower_count * price
    if flower_count > 80:
        total_cost = total_cost - (total_cost * 0.1)

elif flower_type == "Dahlias":
    price = 3.8
    total_cost = flower_count * price
    if flower_count > 90:
        total_cost = total_cost - (total_cost * 0.15)

elif flower_type == "Tulips":
    price = 2.8
    total_cost = flower_count * price
    if flower_count > 80:
        total_cost = total_cost - (total_cost * 0.15)

elif flower_type == "Narcissus":
    price = 3
    total_cost = flower_count * price
    if flower_count < 120:
        total_cost = total_cost + (total_cost * 0.15)

elif flower_type == "Gladiolus":
    price = 2.5
    total_cost = flower_count * price
    if flower_count < 80:
        total_cost = total_cost + (total_cost * 0.20)

money_left = budget - total_cost
if budget >= total_cost:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(money_left):.2f} leva more.")