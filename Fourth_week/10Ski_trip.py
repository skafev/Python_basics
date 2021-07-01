days = int(input()) -1
room_type = input()
feedback = input()
price = 0
discount = 0

if room_type == "apartment":
    if days < 10:
        price = days * 25
        discount = price - (price * 0.3)
    elif 10 < days < 15:
        price = days * 25
        discount = price - (price * 0.35)
    elif days > 15:
        price = days * 25
        discount = price - (price * 0.5)

elif room_type == "president apartment":
    if days < 10:
        price = days * 35
        discount = price - (price * 0.1)
    elif 10 < days < 15:
        price = days * 35
        discount = price - (price * 0.15)
    elif days > 15:
        price = days * 35
        discount = price - (price * 0.2)

elif room_type == "room for one person":
    price = days * 18
    discount = price

if feedback == "positive":
    discount += discount * 0.25
elif feedback == "negative":
    discount -= discount * 0.1

print(f"{discount:.2f}")
