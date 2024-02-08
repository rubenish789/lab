def histogr(arr):
    for i in range(len(arr)):
        print(arr[i]*'*')
    
arr = (list(map(int, input().split())))
histogr(arr)
