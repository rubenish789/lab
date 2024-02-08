def spy_game(arr):
    for i in range(len(arr)-1):
        if arr[i] == 0:
            for j in range (i, len(arr)-1):
                if arr[j] == 0:
                    for m in range (j, len(arr)):
                        if arr[m] == 7:
                            return True
    return False


numbers = list(map(int, input().split()))

print(spy_game(numbers))