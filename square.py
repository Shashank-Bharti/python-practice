'''
Given an integer s, write a program to print the square of size s using "*" character. 
Note: Make sure to add a " " between two "*". Add a new line after printing the square

Examples :

Input: s = 4
Output:
* * * *
*     *
*     *
* * * *
Explanation: It's a square! Each side contains s = 4 *.
Input: s = 3
Output:
* * * 
*   *
* * *
Explanation: It's a square! Each side contains s = 3 *.
Constraints:
1 ≤ s ≤ 10
'''

def square(s):
    for i in range(1,s+1):
        if(i==1 or i==s):
            print("* " * s)
        else:
            print("* ",end="")
            print("  "*(s-2),end="")
            print("*")
    
square(4)