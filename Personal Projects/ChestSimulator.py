#Title Screen
print("""
 _____   __   __   _____    _____   _____     _____   _______   __    __   _     _   __       ___    _____    _____    ______
|  ___| |  | |  | |  ___|  /   __\\ |__ __|   /   __\\ |__   __| |  \\  /  | | |   | | |  |     / _ \\  |__ __|  /  _  \\  |  __  \\
| |     |  |_|  | | |__    \\   \\     | |     \\   \\      | |    |   \\/   | | |   | | |  |    | /_\\ |   | |   |  / \\  | | |__|  |
| |___  |   _   | |  __|  __\\   |    | |    __\\   |   __| |__  |  |\\/|  | |  \\_/  | |  |__  |  _  |   | |   |  \\_/  | |      /
|_____| |__| |__| |_____| \\_____/    |_|    \\_____/  |_______| |__|  |__|  \_____/  |_____| |_| |_|   |_|    \_____/  |__|\\__\\ v1
Created by Christopher Bilodeau


                                             = Press "RETURN" to Continue =
""")

input()

#Main Menu
print("""
: MAIN MENU :

1. Play
2. Password
3. Info

""")

returned = input("Type a number to continue.")

if returned == "1"
    print("1")
if returned == "2"
    print("2")
if returned == "3"
    print("3")
if returned != "1","2","3"
    print("ERROR: Returned input not one of the listed options.")