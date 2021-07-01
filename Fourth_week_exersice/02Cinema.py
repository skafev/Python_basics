text = input()
rows = int(input())
columns = int(input())
price = 0
full_cinema = rows * columns
income = 0

if text == "Premiere":
    price += 12

elif text == "Normal":
    price += 7.5

elif text == "Discount":
    price += 5

income = price * full_cinema
print(f"{income:.2f} leva")

