days = int(input())
food = float(input())
biscuit = 0
dog_food = 0
cat_food = 0

for day in range(1, days+1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())

    if day % 3 == 0:
        biscuit += (food_eaten_by_cat + food_eaten_by_dog) * 0.1

    dog_food += food_eaten_by_dog
    cat_food += food_eaten_by_cat

total_eaten_food =dog_food + cat_food
print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{(total_eaten_food / food) * 100:.2f}% of the food has been eaten.")
print(f"{(dog_food / total_eaten_food) * 100:.2f}% eaten from the dog.")
print(f"{(cat_food / total_eaten_food) * 100:.2f}% eaten from the cat.")
