'''
Given an integer s,  write a program to print a square wall of size s without using string multiplication. Use nested loops instead. The * character will make up the wall.

Before submitting code, verify it by running offline. Does your square visually looks like a square?

Example 1:

Input:
s = 5
Output:

Explanation:
Its perfect square wall. 
Your Task:
The input s is provided as a parameter to the function squareWall. Complete the give code. You do need to provide the new line at the end.squarewall2
'''
def squareWall(s):
    
    #Complete the codes below 
    #Replace .... with your own code
    for i in range(1,s+1):
        
        for j in range(s):
            print("*", end=" ")
        #This print below gives new line, so you don't have to.
        print()
        
squareWall(5)