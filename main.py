import string
import random

len = int(input("How long do you want the password to be: "))

password = list()

for x in range(len):
    flip = random.randint(0, 2)
    match flip:
        case 0:
            password.append(random.choice(string.ascii_letters))
        case 1:
            password.append(random.choice(string.digits))
        case 2:
            password.append(random.choice(string.punctuation))

print(''.join(password))
