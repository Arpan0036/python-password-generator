import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
p_l = int(input("How many letters you want in your password?\n"))
p_n = int(input("How many numbers you want in your password?\n"))
p_s = int(input("How many symbols you want in your password?\n"))
password = []
for _ in range(p_l):
    password.append(random.choice(letters))
for _ in range(p_n):
    password.append(random.choice(numbers))
for _ in range(p_s):
    password.append(random.choice(symbols))
random.shuffle(password)
shuffl_password = ""
for new_p in password:
    shuffl_password = shuffl_password + new_p
print(f"Your password is:  {shuffl_password}")
