#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

d = "AhsjduhduiwhudhuwhdihwidNhiwhn"
x = re.findall('[A-Z][a-z]+', d)
print(x)