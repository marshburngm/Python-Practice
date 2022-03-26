#BMR Equation for men (Harris-Benedict)
#Imperial	BMR = 66 + ( 6.2 × weight in pounds ) + ( 12.7 × height in inches ) – ( 6.76 × age in years )
#age in years
#weight in pounds
#height in inches
# BMI = kg/m**
import time

print('Let us configure BMI and BMR to start calculating caloric intake!\n')

age = int(input('What is your age?\n'))
height = int(input('How tall are you in inches?\n'))
weight = int(input('What is your weight in pounds?\n'))

BMR = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)

print('Your BMR is: \n', round(BMR))

#lets configure BMI
#convert pounds to KG and height to m

kg = weight / 2.2
m = height / 39.37

BMI = int(kg / (m * m))
print('Your BMI is: \n', BMI)

if BMI <= 18.5:
    print('You are classified as underweight.')
if BMI >= 18.5 and BMI <= 24.9:
    print('You are classified as normal weight')
if BMI >=25 and BMI <=29.9:
    print('You are classified as overweight')
if BMI >= 30:
    print('You are classified as obese')
time.sleep(3)

print('\nNow one more step to complete before calculating calories to eat for weight loss!\n')
#TDEE = BMR + Activity Level

while True:
    activity_level = (input('Are you sedentary, lightly active, moderately active or very active?\n'))
    if activity_level == 'sedentary':
        TDEE = BMR * 1.2
        print('Your Total Daily Energy Expenditure (TDEE) is: ',round(TDEE))
        break
    elif activity_level == 'lightly active':
        TDEE = BMR * 1.375
        print('Your Total Daily Energy Expenditure (TDEE) is: ',round(TDEE))
        break
    elif activity_level == 'moderately active':
        TDEE = BMR * 1.725
        print('Your Total Daily Energy Expenditure (TDEE) is: ',round(TDEE))
        break
    elif activity_level == 'very active':
        TDEE = BMR * 1.9
        print('Your Total Daily Energy Expenditure (TDEE) is: ',round(TDEE))
        break
    else: 
        print('Sorry, cannot compute!')
time.sleep(2)        

print('\nNow we can figure out how much weight we can lose, safely, per week!\n')
time.sleep(2)
print('Let us start at 1 pound per week!\n')
time.sleep(2)
print('To safely lose 1 pound per week, we must take your TDEE - 500 calories.\n')
time.sleep(2)
cals_per_day = TDEE - 500
print('Your recommended caloric intake per day is: ', round(cals_per_day))
