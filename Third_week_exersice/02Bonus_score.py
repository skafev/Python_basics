number = int(input())
bonus_scores = 0

if number <= 100:
    bonus_scores = 5
elif 100 < number < 1000:
    bonus_scores = number * 0.2
else:
    bonus_scores = number * 0.1

if number % 2 == 0:
    bonus_scores += 1
elif number % 5 == 0:
    bonus_scores += 2

total_score = number + bonus_scores
print(bonus_scores)
print(total_score)