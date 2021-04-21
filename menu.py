# basic menu for python

menu = { '1': "one",
         '2': "two",
         '3': "three"

}

print("Please choose (0 to quit)")
for choice in menu:
    print(f"\t {choice} - {menu[choice]}")

while True:
    choice = input()

    if choice == '0':
        print("Good bye")
        break

    if choice in menu.keys():
        print(f"You chose {choice}")