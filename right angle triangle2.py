'''
Given an integer s. Write a program to print the Right angle triangle. The length of the perpendicular and base is s.  Use single loop and string multiplication.

Example 1:

Input:
s = 9
Output:
*
*  *
*    *
*      *
*        *
*          *
*            *
*              *
* * * * * * * * * 
Explanation:
Length of perpendicular and base of triangle is 9 .
Your Task:
The input s is provided as a parameter to the function triangle. Complete the given code so that a triangle is printed and new line is provided at the end.
'''
def triangle(s):
    #Complete the code given below
    #Replace ..... by your own code
    for i in range(s):
        if i == 0:
            print("* ")
            
        elif i == s-1 :
            print("* "*s)
            
        else:
            print("*",end="")
            print(" " * (i+i), end="")
            print("*")
            
triangle(9)