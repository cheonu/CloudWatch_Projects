from random import choice

length_of_password=8
valid_x_password_char="#$%&'()*+,-./0123456789:;<=>?@ABstuvwxyz"

password=[]
for each_char in range(length_of_password):
    password.append(choice(valid_x_password_char))

random_pasword="".join(password)
print(random_pasword)

