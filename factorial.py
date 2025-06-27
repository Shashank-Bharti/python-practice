'''
Given an integer n. Write a program to return the factorial of n.
Factorial of a number is the product of all the numbers from 1 till n.

Note: 0 factorial is equal to 1.

Example:

Input: n = 5
Output: 120
Explanation: 1 * 2 * 3 * 4 * 5 = 120
Input: n = 10
Output: 3628800
Explanation: 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800
'''

def nFactorial(n):

    ans = 1
    #Write your code below
    for i in range (1,n+1):
        ans = ans*i
    return ans

print(nFactorial(5))