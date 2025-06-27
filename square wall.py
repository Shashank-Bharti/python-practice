'''
Given an integer s,  write a program to print the square wall of size s using single loops. Use * character to make the wall.

Note: Use string multiplication for Python.

Before submitting the code, verify it by running offline. Does your square visually look like a square?

Example 1:

Input:
s = 5
Output:

Explanation:
Its perfect square wall. 
Your Task:
You are given s as a parameter to the function squareWall. Just complete the provided code and print the output. You do need to provide a new line at the end.
 

Constraints:
1 ≤ s ≤ 10
'''

def squareWall(s):
    for i in range(s):
       print("* "*s,end="")
       if i != s-1:
         print()                                         
            
squareWall(5)