price_for_vacation = float(input())
puzzles_sold = int(input())
talking_dolls_sold = int(input())
teddy_bears_sold = int(input())
minions_sold = int(input())
trucks_sold = int(input())

total_toys_sold = puzzles_sold + talking_dolls_sold + teddy_bears_sold + minions_sold + trucks_sold
total_income = (puzzles_sold * 2.6) + \
               (talking_dolls_sold * 3) + \
               (teddy_bears_sold * 4.1) + \
               (minions_sold * 8.2) + \
               (trucks_sold * 2)

if total_toys_sold >= 50:
    total_income = total_income - (total_income * 0.25)

total_income = total_income - (total_income * 0.1)
left_money = total_income - price_for_vacation
if total_income >= price_for_vacation:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {abs(left_money):.2f} lv needed.")