#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
import re

text = "hdsbbdhbd_dyg3gs56s5hbhbdhjbhab"
x = re.findall('^.*a.*b$', text)   #. -- Any character (except newline character)
print(x)