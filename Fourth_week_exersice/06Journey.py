budget = float(input())
season = input()
where_will_stay = ""
where_will_go = ""

if budget <= 100:
    where_will_go = "Bulgaria"
    if season == "summer":
        where_will_stay = "Camp"
        budget *= 0.30
    elif season == "winter":
        where_will_stay = "Hotel"
        budget *= 0.70

elif budget <= 1000:
    where_will_go = "Balkans"
    if season == "summer":
        where_will_stay = "Camp"
        budget *= 0.40
    elif season == "winter":
        where_will_stay = "Hotel"
        budget *= 0.80
else:
    where_will_go = "Europe"
    where_will_stay = "Hotel"
    budget *= 0.90

print(f"Somewhere in {where_will_go}")
print(f"{where_will_stay} - {budget:.2f}")