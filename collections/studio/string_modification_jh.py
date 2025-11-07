my_string = 'LaunchCode'

# a) Use string methods to remove the first three characters from the string and add them to the end.
new_string = my_string[0:3]
changed_string = my_string[3:len(my_string)]
changed_string = changed_string + new_string
print(new_string)
print(my_string)
print(changed_string)

# Use a template literal to print the original and modified string in a descriptive phrase.
print(f"The original string is {my_string} and the modified string is {changed_string}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
word_length = len(my_string)
print(f"Enter the number of letters to be relocated. Must be greater that 0 and less than {word_length}")
user_input = int(input("Enter Number: "))



# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
num_tries = 0
while user_input < 0 or user_input > word_length:
    num_tries += 1
    if num_tries >= 3:
        print(f"You tried {num_tries} which is the max attempts. The default value of 3 will be used.")
        user_input = 3
        break
    else:
        print(f"Enter the number of letters to be relocated. Must be greater that 0 and less than {word_length}")
        user_input = int(input("Enter Number: "))
    
new_string = my_string[0:user_input]
changed_string = my_string[user_input:word_length]
changed_string = changed_string + new_string
print(user_input)
print(new_string)
print(changed_string)