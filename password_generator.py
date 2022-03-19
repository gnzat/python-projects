import string
import random

## characters to generate password from
alphabets = list(string.ascii_letters) #string.ascii_letters - concatenation of ascii_lowercase and ascii_uppercase string constants.
digits = list(string.digits) #the string '0123456789'
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Enter password length: ")) #int - converts it to integer value

	## number of character types
	alphabets_count = int(input("Enter alphabets count in password: "))
	digits_count = int(input("Enter digits count in password: "))
	special_characters_count = int(input("Enter special characters count in password: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	## check the total length with characters sum count
	## print not valid if the sum is greater than length
	if characters_count > length:
		print("Characters total count is greater than the password length")
		return

	## initializing the password
	password = []
	
	## picking random alphabets
	for i in range(alphabets_count):
		password.append(random.choice(alphabets)) #.append takes an object as an argument and adds it to the end of an existing list, right after its last element:

	## picking random digits
	for i in range(digits_count):
		password.append(random.choice(digits))


	## picking random alphabets
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	## if the total characters count is less than the password length
	## add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string, join them all into a string
	## printing the list
	print("".join(password))



## invoking the function
generate_random_password()