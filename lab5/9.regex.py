#Write a Python program to insert spaces between words starting with capital letters
import re
def space(x):
    
    return (re.findall('[A-Z][a-z]*', x))
    

x = "INDINidsmaoidmisdiaimJMos"
print(space(x))