def has_33(arr):
    for i in range(len(arr)-1):
        if(arr[i] == arr[i+1] == 3):
            return True
    return False

"""n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)"""
    
numbers = list(map(int, input().split()))

print(has_33(numbers))