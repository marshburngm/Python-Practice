#Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number 
#of times the character appears in the phrase.

# take the string input from user
string = input()
count = 0  
   
#Count
for i in range(2, len(string)):  
    if(string[i] == string[0]):  
        count = count + 1;  
   
#Displays the character count in given string 
print(str(count))

