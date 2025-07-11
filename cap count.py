s = "ab cd ef gh"
# count = 0
# for i in (s.split(" ")):
#     print(i.capitalize(),end=" ")
#     count += 1
# print()
# print(count)
class Solution:
    
    def capCount(self,s):
        # Code here to print after captilizing first letter of all string
        self.count = 0
        for i in (s.split(" ")):
            print(i.capitalize(),end=" ")
            self.count += 1 
        # and then print the count of number of words
        print()
        print(self.count)
        # Your code should provide a new line after printing
        
Solution().capCount(s=s)