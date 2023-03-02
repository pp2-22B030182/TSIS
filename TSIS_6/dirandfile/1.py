import os

with os.scandir('papka1') as entries:
    print("File and directories:")
    for entry in entries:
        print(entry.name)