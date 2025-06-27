'''
You are given a number n, you need to print its multiplication table in a single line.

Note: Please go through the range function in the video tutorial(for Python).

Example:
Input:
n = 5
Output:
5 10 15 20 25 30 35 40 45 50

Your Task:
This input is taken care of the given code. You just need to complete the code at the mentioned places.
'''


#User function Template for python3


def utility():
    n = int(input("Enter a number: "))  ## Taking input from user
    ## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11):  ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i * n, end=" ")  ## Separating by spaces using end =" "


utility()