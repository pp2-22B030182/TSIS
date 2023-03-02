import os

a = input()

print("existance:", os.access(a, os.F_OK))

print("Readability:", os.access(a, os.R_OK))

print("Writability:", os.access(a, os.W_OK))

print("Executability:", os.access(a, os.X_OK))