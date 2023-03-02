import os


if os.access('papka1', os.F_OK):
    print("existance:",True)

os.remove('papka1/1.py')