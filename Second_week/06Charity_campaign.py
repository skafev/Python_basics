days_campaign = int(input())
count_of_bakers = int(input())
count_of_cakes = int(input())
count_of_waffles = int(input())
count_of_pancakes = int(input())

cake_price = count_of_cakes * 45
waffles_price = count_of_waffles * 5.8
pancakes_price = count_of_pancakes * 3.2
total_price = (cake_price + waffles_price + pancakes_price) * count_of_bakers
final_price = (total_price * days_campaign) - ((total_price * days_campaign) / 8)

print(final_price)