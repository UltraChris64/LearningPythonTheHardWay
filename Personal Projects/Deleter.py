import os

file = input("Which file would you like to remove?: ")

os.remove(file)
print(f"{file} Removed!")