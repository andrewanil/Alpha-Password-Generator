# Alpha Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Alpha Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_letters = random.choice(letters)
for i in  range (1, nr_letters):
  rand_letters += random.choice(letters)

rand_symbols = random.choice(symbols)
for i in  range (1, nr_symbols):
  rand_symbols += random.choice(symbols)

rand_numbers = random.choice(numbers)
for i in  range (1, nr_numbers):
  rand_numbers += random.choice(numbers)

password = [rand_letters.lower(), rand_symbols.lower(), rand_numbers.lower()]

random.shuffle(password)

password_list = ""
for i in password:
  password_list += i

print(f"Your password is: {password_list} ")