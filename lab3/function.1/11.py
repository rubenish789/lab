def is_poli(str):
    for i in range(len(str)//2):
        if str[i] != str[-i-1]:
            return False
    return True

str = input()
print(is_poli(str))