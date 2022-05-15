#Many documents use a specific format for a person's name. Write a program whose input is: firstName middleName lastName
#and whose output is: lastName, firstInitial.middleInitial.

#get input name and convert 
name=input().split()

#check if there is middle name
if(len(name)==3):
    #print name in required order
    print(name[2]+", "+name[0][0]+"."+name[1][0]+".")

#check if there is only first and last name

elif(len(name)==2):
    #printing name in required order
    print(name[1]+", "+name[0][0]+".")
    
