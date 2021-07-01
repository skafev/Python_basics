income = float(input())
average_score = float(input())
min_wage = float(input())
nerd_scholarship = 0
social_scholarship = 0

if average_score >= 5.5:
    nerd_scholarship = average_score * 25

if income < min_wage and average_score > 4.5:
    social_scholarship = min_wage * 0.35

if income > min_wage and average_score < 5.5:
    print ("You cannot get a scholarship!")
elif social_scholarship <= nerd_scholarship:
    print (f"You get a scholarship for excellent results {int(nerd_scholarship)} BGN")
else:
    print (f"You get a Social scholarship {int ( social_scholarship )} BGN")