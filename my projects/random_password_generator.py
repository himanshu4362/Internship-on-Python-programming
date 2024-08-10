import random
import string
c_string = ""
c_string += string.ascii_letters + string.digits + string.punctuation
password = ""
n = int(input("enter the length of your password :"))
for i in range(n): 
    choosed_charector = random.choice(c_string)
    password += choosed_charector 
print("your Password is :",password)
