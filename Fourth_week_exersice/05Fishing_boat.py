budget = int(input())
season = input()
number_of_fishermens = int(input())
boat_rental_price = 0
price = 0

if season == "Spring":
    boat_rental_price = 3000
    if number_of_fishermens <= 6:
        price = boat_rental_price - (boat_rental_price * 0.1)
    elif number_of_fishermens <= 11:
        price = boat_rental_price - (boat_rental_price * 0.15)
    else:
        price = boat_rental_price - (boat_rental_price * 0.25)

elif season == "Summer" or season == "Autumn":
    boat_rental_price = 4200
    if number_of_fishermens <= 6:
        price = boat_rental_price - (boat_rental_price * 0.1)
    elif number_of_fishermens <= 11:
        price = boat_rental_price - (boat_rental_price * 0.15)
    else:
        price = boat_rental_price - (boat_rental_price * 0.25)

else:
    boat_rental_price = 2600
    if number_of_fishermens <= 6:
        price = boat_rental_price - (boat_rental_price * 0.1)
    elif number_of_fishermens <= 11:
        price = boat_rental_price - (boat_rental_price * 0.15)
    else:
        price = boat_rental_price - (boat_rental_price * 0.25)

if number_of_fishermens % 2 == 0 and season != "Autumn":
    price = price - (price * 0.05)

money_left = budget - price
if budget >= price:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")