#Write a Python program to convert a given camel case string to snake case.
import re
def com(s):
    res = ' '
    res += (s.group()).lower()
    return res

s = input()
snake = re.sub(r'([A-Z])', com, s) 
print(snake)    