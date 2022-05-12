#With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). 
#And then the program should print the dictionary.

def showSquared(num):
    squared = {}
    for i in range(1, num+1):
        squared[i] = i*i
    print(squared)
    
