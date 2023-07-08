import random
password = ""
password_variables = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len1 = int(input("Введите длинну вашего пароля."))
for i in range(len1):
    password += random.choice(password_variables)
print(range(5))
print(password)





