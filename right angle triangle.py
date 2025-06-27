'''
Given an integer s. Write a program to print the Right angle triangle wall. The length of perpendicular and base is s.  Use single loop and string multiplication.

Note: Print exactly single " " after "*". Print a new line after printing the triangle.

Examples:

Input: s = 4
Output:
* 
* * 
* * * 
* * * * 
Explanation: Length of perpendicular and base of triangle is 4 .
Input: s = 3
Output:
* 
* * 
* * * 
Explanation: Length of perpendicular and base of triangle is 3 .
'''

def triangleWall(s):
    #Complete the given code
        for i in range(1,s+1):
            print("* " * i,end="")
            print()
            
triangleWall(5)