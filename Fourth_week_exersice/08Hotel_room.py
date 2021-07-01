month = input()
nights = int(input())
price_for_apartment = 0
price_for_studio = 0

if month == "May" or month == "October":
    price_for_studio = 50
    price_for_apartment = 65
    if nights > 14:
        price_for_studio = price_for_studio - (price_for_studio * 0.3)
    elif nights > 7:
        price_for_studio = price_for_studio - (price_for_studio * 0.05)

elif month == "June" or month == "September":
    price_for_studio = 75.2
    price_for_apartment = 68.7
    if nights > 14:
        price_for_studio = price_for_studio- (price_for_studio * 0.2)

elif month == "July" or month == "August":
    price_for_studio = 76
    price_for_apartment = 77

if nights > 14:
    price_for_apartment = price_for_apartment - (price_for_apartment * 0.1)

total_apartment = price_for_apartment * nights
total_studio = price_for_studio * nights

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv. ")
