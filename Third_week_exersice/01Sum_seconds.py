athlete_a = int(input())
athlete_b = int(input())
athlete_c = int(input())
total_time = athlete_a + athlete_b + athlete_c

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")