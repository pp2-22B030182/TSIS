import os

a = input()

if os.access(a, os.F_OK):
    with os.scandir(a) as x:
        print("File and Directories:")
        for i in x:
            print(i.name)