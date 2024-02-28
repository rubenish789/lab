#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re
 
b="Hello, World pdscp...skcns"
x=re.sub("[.]|[,]|[ ]", ":", b)
print(x)