print('Hi there')     #say hi :)
print('insert number:')   #ask user to insert number

num = float(input())   #float because user may input a decimal

#if statement to state out conditions
if num > 0:
    print('the number is a POSITIVE number')   #if number input is greater than zero then its definitely positive
elif num < 0:
    print('the number is a NEGATIVE number')   #if number input is less than zero then its definitely negative
else:
    print('number is equal to ZERO!')          #if it is neither positive or negative then its value is ZER0

print('Thank you!')                        #Thank you :)