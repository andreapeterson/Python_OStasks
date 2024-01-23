#!/usr/bin/python3

import os
path = input("Enter path to see if it is a file, directory, or doesn't exist: ")

if os.path.isdir(path):
    print("It is a directory.")
elif os.path.isfile(path):
    print("It is a file.")
else:
    print("File or directory does not exist.")
