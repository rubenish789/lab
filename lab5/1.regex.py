#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s

import re

def match(a, b):
    return bool(re.search(a,b))

a='a.*b'
b= ['a', 'ab', 'ac', 'abb', 'bc', 'abbb', 'acc']
for x in b:
    if match(a, x):
        print(f"'{x}' Matches")
    else:
        print(f"'{x}' Doesn't match")