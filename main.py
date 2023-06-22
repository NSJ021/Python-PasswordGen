#Password Generator Project
import random
# List of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# List of Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# List of symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Title and Inputs
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""   # Declare password string

# For loop to get randomised selection from list of letters
for char in range (1, nr_letters + 1):  # range, start at 1, using the input value plus 1, plus 1 needed as index would be to short for the required amount.
    password += random.choice(letters)  #Adds the randomised letter to the password variable

# For loops to get randomised selection from list of symbols
for char in range (1, nr_symbols + 1):
    password += random.choice(symbols)

# For loops to get randomised selection from list of numbers
for char in range (1, nr_numbers + 1):
    password += random.choice(numbers)

# Converting password string into a list, which can then be shuffled via random.shuffle(), this returns a list so the "".join() method coverts the list back to a string

password_shuffled = list(password) 
random.shuffle(password_shuffled)
print ("".join(password_shuffled))

# ---------------------------------------- Another approach would be to add each for loop iteration into a list ---------------------------------------
#
# -----------------------------------------------------------------------------------------------------------------------------------------------------

password_list = []   # Declare password string

# For loop to get randomised selection from list of letters
for char in range (1, nr_letters + 1):  # range, start at 1, using the input value plus 1, plus 1 needed as index would be to short for the required amount.
    password_list += random.choice(letters)  #Adds the randomised letter to the password variable

# For loops to get randomised selection from list of symbols
for char in range (1, nr_symbols + 1):
    password_list += random.choice(symbols)

# For loops to get randomised selection from list of numbers
for char in range (1, nr_numbers + 1):
    password_list += random.choice(numbers)

# password2 list, which can then be shuffled via random.shuffle(), this returns a list so the "".join() method coverts the list back to a string

print(password_list)
random.shuffle(password_list)
print("".join(password_list))
