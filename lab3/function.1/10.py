def unique_elems(arr):
    list = []
    for i in arr:
        if i not in list:
            list.append(i)
    return list

numbers = list(map(int, input().split()))

print(unique_elems(numbers))