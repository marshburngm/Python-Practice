#Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program: 8 Then, the output should be:4032

def findFactorial(num):
    sum = 1
    for i in range(1, num+1):
        sum = sum * i
    print(sum)
    
