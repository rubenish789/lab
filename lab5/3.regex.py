#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

def match(a,b):
    return bool(re.search(a, b))

a="[a-z]*_"
b=['love_kitty_', 'HFghsu', 'h_e_l_lo', 'dgcu']

for x in b:
    if match(a, x):
        print(f"'{x}' Matches!")
    else:
        print(f"'{x}' Doesn't match")