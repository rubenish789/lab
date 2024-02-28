#Write a python program to convert snake case string to camel case string.
import re
def snake(s):
    res = ''
    res += (s.group()).upper()
    return res

str = input()
cam = re.sub(r'(_[a-z])', snake, str)
cam = cam.replace('_', '')
print(cam)