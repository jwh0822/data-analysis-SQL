food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_list = sorted(food.split(','))
equipment_list = sorted(equipment.split(','))
pets_list = sorted(pets.split(','))
sleep_list = sorted(sleep_aids.split(','))


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_list, equipment_list, pets_list, sleep_list]
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
cabinet_num = int(input("Select a cabinet (0-3): "))


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
while cabinet_num < 0 or cabinet_num > 3:
    print(f"You entered {cabinet_num}! That's and invalid entry! Try Again!")
    cabinet_num = int(input("Select a cabinet (0-3):"))
print(f"You entered cabinet number {cabinet_num}")
print(f"Cabinet Contents {cargo_hold[cabinet_num]}")


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
another_try = 'Y'

while another_try == 'Y':
    cabinet_num = int(input("Select a cabinet (0-3):"))
    while cabinet_num < 0 or cabinet_num > 3:
        print(f"You entered {cabinet_num}! That's and invalid entry! Try Again!")
        cabinet_num = int(input("Select a cabinet (0-3):"))

    user_item = input("Enter a particular item: ")

    if user_item in cargo_hold[cabinet_num]:
        print(f"Cabinet {cabinet_num} contains {user_item}")
    else:
        print(f"Cabinet {cabinet_num} does not contain {user_item}")
    another_try = input("Try Again? (Y/N): ")
    another_try = another_try.upper()

