# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
a_slice = text[0:12]
print(a_slice)

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
print(text[-12:])

# 3. Print a slice of the middle 12 characters from 'text'.
print(text[12:24])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
a_word = 'word' 
for x in range(len(a_word)-1,-1,-1):
    print(a_word[x])

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
a_word = "good"
new_word = ""
for x in range(len(a_word)-1,-1,-1):
    new_word = new_word + a_word[x]
print(new_word)
# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
new_word =""
for x in range(len(word)-1,-1,-1):
    new_word = new_word + word[x]
print(word + new_word)
print(word + " | " + new_word)