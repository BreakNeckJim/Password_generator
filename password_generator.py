import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
numbers = "0123456789"
symbols = "~!@#$%^&*()_+"

ans = lowercase + uppercase + numbers + symbols

length = 10
password = "".join(random.sample(ans, length))

print("Generated password is: ", password)