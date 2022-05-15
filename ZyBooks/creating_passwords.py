

# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
pet = input("Enter pet's name:\n")
number = input('Enter a number:\n')

print('You entered:',favorite_color,pet,number)

# FIXME (2): Output two password options
#make password combinations 1 & 2 
password1 = favorite_color+'_'+pet
password2 = number + favorite_color + number
#print results
print("\nFirst password: " + password1)
print("Second password: " + password2)

# FIXME (3): Output the length of the two password options
#compile and print output of lent of 2 passwords
print("\nNumber of characters in " + password1+ ': ' +str(len(password1)))
print("Number of characters in " + password2+ ': ' +str(len(password2)))

