price_of_whiskey = float(input())
amount_of_beer = float(input())
amount_of_wine = float(input())
amount_of_rakia = float(input())
amount_of_whiskey = float(input())

price_of_rakia = price_of_whiskey / 2
price_of_wine = price_of_rakia - (0.4 * price_of_rakia)
price_of_beer = price_of_rakia - (0.8 * price_of_rakia)

final_beer = price_of_beer * amount_of_beer
final_wine = price_of_wine * amount_of_wine
final_rakia = price_of_rakia * amount_of_rakia
final_whiskey = price_of_whiskey * amount_of_whiskey

total = final_beer + final_wine + final_rakia + final_whiskey

print(f"{total:.2f}")
