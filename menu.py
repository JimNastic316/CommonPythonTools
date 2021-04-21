# basic menu for python

menu = { '1': "one",
         '2': "two",
         '3': "three"

}

# print("Please choose (0 to quit)")
# for choice in menu:
#     print(f"\t {choice} - {menu[choice]}")

while True:
    print("Please choose (0 to quit)")
    for choice in menu:
        print(f"\t {choice} - {menu[choice]}")


    choice = input("Enter your selection: ")
    print(f"You chose {choice}")

    if choice == '0':
        print("Good bye")
        break

    elif choice in menu.keys():
        print(f"{choice} is valid")

    else:
        print(f"{choice} is invalid, try again")