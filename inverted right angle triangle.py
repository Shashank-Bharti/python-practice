'''
Given an integer s. Write a program to print the Inverted "Right angle triangle" wall. The length of the perpendicular and base is s.  Use a single loop and string multiplication.

Examples:

Input: S = 4
Output:
* * * * 
* * * 
* * 
*
Explanation: Length of perpendicular and base of triangle is 4 .
Input: S = 3
Output:
* * * 
* * 
*
Explanation: Length of perpendicular and base of triangle is 3 .
'''

def invTriangleWall(s):
    #Complete the given code
    for i in range (s,0,-1):
        if i == s:
            print("* "*s)
        else:
            print("* "*i,end="")
            print()
        
    
invTriangleWall(5)