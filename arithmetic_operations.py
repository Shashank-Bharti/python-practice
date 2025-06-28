'''
You are given two integer variables x and y. You need to perform the following operations:

p = x+y : Addition
q = x-y : Subtraction
r = x*y :Multiplication
s = x/y : Float Division with a precision of 5 decimal places
t = x//y : Int Division
u = x%y : Modulo
v = x**y : Power
Examples:

Input: x = 1, y = 2
Output: 3 -1 2 0.50000 0 1 1 
Explanation: The given operations are performed.
Input: x = 3 ,y = 4 
Output: 7 -1 12 0.75000 0 3 81
Explanation: The given operations are performed
'''
def utility(x, y):
    # Perform addition x+y below
    p = (x+y)
    # Perform subtraction x-y below
    q = (x-y)
    # Perform multiplication x*y below
    r = (x*y)
    # Perform float division x/y below
    s = (x/y)
    # Perform integer divison x//y below
    t = (x//y)
    # Perform modulo operation x%y below
    u = (x%y)
    # Perform power(x,y) x**y below
    v = (x**y)
    
    #The below code prints the output. Don't change it!
    print(p,q,r,"{:.5f}".format(s),t,u,v)
    
utility(x=5,y=10)