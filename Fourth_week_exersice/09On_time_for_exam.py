hour_for_exam = int(input())
minutes_for_exam = int(input())
hour_arrived = int(input())
minutes_arrived = int(input())
time_arrived = 0
on_time = 0

if hour_for_exam >= hour_arrived:
    if minutes_arrived + 31 <= minutes_for_exam + 60:
        time_arrived = 60 - (minutes_arrived % 60)
        on_time = time_arrived + minutes_for_exam

        if on_time > 59:
            on_time = on_time - 60
            print(f"Early {hour_for_exam - hour_arrived}:{on_time} minutes before the start")
        else:
            print(f"Early {on_time} minutes before the start")

    if minutes_arrived + 30 <= minutes_for_exam + 60:
        time_arrived = 60 - (minutes_arrived % 60)
        on_time = time_arrived + minutes_for_exam
        print(f"On time {on_time} before the start")
else:
    if hour_arrived > hour_for_exam:
        if minutes_arrived <= minutes_for_exam + 60 :
            time_arrived = 60 - (minutes_arrived % 60)
            on_time = time_arrived + minutes_for_exam

            if on_time > 59 :
                on_time = on_time - 60
                print (f"late")
            else :
                print (f"late")


exam_hour = int(input()) * 60
exam_minutes = int(input())
arrive_hour = int(input()) * 60
arrive_minutes = int(input())

if exam_hour + exam_minutes < arrive_hour + arrive_minutes:
    print("Late")
    if exam_hour < arrive_hour:
        exam_minutes += 60
        print(f"{abs(exam_hour -  arrive_hour) // 60} : {exam_minutes - arrive_minutes}")

elif exam_hour + exam_minutes <= arrive_hour + arrive_minutes + 30:
    print("On time")
else:
    print("Early")
    if exam_hour > arrive_hour:
        exam_minutes += 60
        if exam_minutes > 59:
            exam_hour += 60
            exam_minutes -= 60
        exam_hour -= 60
        if exam_hour == arrive_hour:
            print(f"{exam_minutes - arrive_minutes}")
        else:
            print(f"{(exam_hour - arrive_hour) // 60} : {exam_minutes - arrive_minutes}")