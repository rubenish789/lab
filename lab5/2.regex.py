#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

def match(a, c):
    return bool(re.search(a,c))

a='ab{2}$|ab{3}$'
c=['ab', 'abb', 'abbbb', 'acb', 'abb','bv', 'abbb' ]

for x in c:
    if match(a, x):
        print(f"'{x}' Matches!")
    else:
        print(f"'{x}' Doesn't match")