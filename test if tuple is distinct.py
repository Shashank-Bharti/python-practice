


arr = tuple(map(int, input().split()))

set = set()
def check(arr):
    for item in arr:
        
        if item in set:
            return False
        set.add(item)    

    return True    
        
print(check(arr))