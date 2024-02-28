#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

txt = 'shdhiwi_jd_ij_di_dksdkals_smam'

x = re.findall('[a-z]*_', txt)
print(x)