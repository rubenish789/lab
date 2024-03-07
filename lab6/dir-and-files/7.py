#Write a Python program to copy the contents of a file to another file

import shutil
import os

def copy(file, new_file):
    if os.path.isfile(file):
        shutil.copyfile(file, new_file)
        print("The file has been copied successfully!")
    else:
        print("The source file could not be found.")

file = "C:/Users/mayta/Desktop/KBTU/pp/python/lab6/dir-and-files/7file.txt"
new_file ="C:/Users/mayta/Desktop/KBTU/pp/python/lab6/dir-and-files/7newfile.txt"
copy(file, new_file)