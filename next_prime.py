'''
Given an integer n. Write a program to find the first prime number greater than n.

Examples:

Input: n = 15
Output: 17
Explanation: 17 is next prime number.
Input: n = 7
Output: 11
Explanation: 11 is the prime number next to 7.
Constraints:
1 <= n <= 500
'''

def nextPrime(n):
    if n <= 1:
        return "Invalid Input"
    
    x = n + 1
    while True:
        is_prime = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            return x
        x += 1

print(nextPrime(21))