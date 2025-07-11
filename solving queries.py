'''
Given a dictionary, and a list of queries(keys), you have to find and print the value of each query from the dictionary if present else it prints "None".

Examples:

Input:
dict = {1:"abc", 2: "cde", 3: "fgh"}
query = [2, 3, 4]
Output:
cde
fgh
None

'''
dict = {1:"abc", 2: "def", 3: "ghi"}
query = [2, 3, 4]


class Solution:
    
    def Query(self, dict, query):
        # return a list of query outputs
        results = []
        for key in query:
            if key in dict:
                value = dict[key]
                results.append(value)
            else:
                results.append(None)
        
        for res in results:
            print(res)
        
        
    
print(Solution().Query(dict,query))