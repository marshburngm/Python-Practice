#Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. 
#Output the average calories burned for a person.

''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
''' Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''

Age = input()
weight = input()
Heart_Rate = input()
Time = input()

Men_calories = ((float(Age) * 0.2017) + (float(weight) * 0.09036) + (float(Heart_Rate) * 0.6309) - 55.0969) * float(Time) / 4.184
Women_calories = ((float(Age) * 0.074) - (float(weight) * 0.05741) + (float(Heart_Rate ) * 0.4472) - 20.4022) * float(Time) / 4.184

print('Women: {:.2f} calories'.format(Women_calories))
print('Men: {:.2f} calories'.format(Men_calories))

