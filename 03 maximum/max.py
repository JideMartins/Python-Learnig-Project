# Maximum of 3 numbers

print("This code finds the maximum of 3 numbers x, y and z")
x = float(input('insert first number: '))
y = float(input('insert second number: '))
z = float(input('insert third number: '))

print('maximum of the 3 values is: ', end='')
if y <= x >= z:
    print(x)
elif x <= y >= z:
    print(y)
elif x <= z >= y:
    print(z)

print('Cheers Mate')


#NOTE to be revised with the list version where any amount of numbers can be compared