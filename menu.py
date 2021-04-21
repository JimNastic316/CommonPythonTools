# basic menu for python

menu = { '1': "one",
         '2': "two",
         '3': "three"

}

print("Please choose (0 to quit)")
for choice in menu:
    print(f"\t {menu[choice]}")