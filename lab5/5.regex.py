#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

b = "oihudfrdjaanvflsbjsk_kcbabjabaabb"
x = re.findall('^.*a.*b$', b)   
print(x)