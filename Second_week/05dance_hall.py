import math

length = float(input())
width = float(input())
wardrobe = float(input())

hall_size = (length * 100) * (width * 100)
bench = hall_size / 10
wardrobe_size = wardrobe *100 * wardrobe * 100
dancers_space = 70.40
hall_needed_space = hall_size - bench - wardrobe_size
dancers = hall_needed_space / dancers_space

print(round(dancers))