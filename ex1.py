name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f'Hello {name}. After you will turn 100 on {2022-age+100}')

# ******* For extra 1
msg = f'Hello {name}. After you will turn 100 on {2022-age+100}'
extra1 = int(input("Enter your extra: "))
print(msg*extra1)

# ****** For extra 2
print((msg+'\n')*extra1)
