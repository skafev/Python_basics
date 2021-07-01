import math
year = input()
holiday = int(input())
weekends = int(input())

weekends_to_play = (48 - weekends) * 0.75
holiday_can_play = holiday * 2/3
playing_volleyball = weekends_to_play + weekends + holiday_can_play

if year == "leap":
    playing_volleyball += playing_volleyball * 0.15
    print(math.floor(playing_volleyball))
else:
    print(math.floor(playing_volleyball))