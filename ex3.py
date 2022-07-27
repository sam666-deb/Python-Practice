a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in range(len(a)):
    if a[i] < 5:
        print(a[i])

# ********* Extra 1

li2 = []

for i in range(len(a)):
    if a[i] < 5:
        li2.append(a[i])
print(li2)


# ********* Extra 2

num1 = int(input('Enter a number: '))
li3 = []
for i in range(len(a)):
    if a[i] < num1:
        li3.append(a[i])
print(li3)
