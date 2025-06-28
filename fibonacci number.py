'''
Given an integer n. Write a program to find the nth Fibonacci number.
The nth Fibonacci number is given by the forumla F(n)=F(n-1)+F(n-2). The first few fibonacci numbers are: 
1 1 2 3 5... and so on

Example 1:

Input:
n = 4
Output: 
3
Explanation:
In the series 1 1 2 3 5...... the fourth fibonacci number is 3.
Example 2:

Input:
n = 6
Output: 
8
Explanation:
In the series 1 1 2 3 5 8 13...... the sixth fibonacci number is 8.
Your Task:
The input n is provided as a parameter to the function fibonacci. Complete the given code so that it returns the nth Fibonacci number Number. Don't print anything.
'''
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    prev_term = 1
    next_term = 1
    
    for i in range(3, n + 1):
        temp = prev_term + next_term
        prev_term = next_term
        next_term = temp
    
    return next_term

n = 4
result = fibonacci(n)
print(result)

# gfg soln.
'''
def fibonacci(n):
    n=n-1
    
    if n == 0 or n == 1:
        return 1
    a = b = 1

    c = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return c
'''