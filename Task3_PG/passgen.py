import random
import string

print("---PASSWORD GENERATOR---")
len = int(input("Enter the Lenght of your Password: "))
if len < 3:
    print("Password must contain at least 3 characters.")
else:
    chars = string.ascii_letters + string.digits + string.punctuation 
    password = [random.choice(string.digits),random.choice(string.ascii_letters),random.choice(string.punctuation)] 
    for _ in range(len - 3):
        password.append(random.choice(chars))
    random.shuffle(password)
    generated_password = ''.join(password)
    print("Your Password is: ",generated_password)
