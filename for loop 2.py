'''
You are given a String S, you need to print its characters at even indices(index starts at 0).
Input: s = "Geeks"
Output: Ges
Explanation: The even indices characters are printed.

Expected Complexities
Time Complexity: O(n)
Auxiliary Space: O(1)

'''

def utility(s):
    #code here
    for i in range(0, len(s),2):
        print(s[i], end="")