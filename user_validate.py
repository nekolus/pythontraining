# Simple if else
a = 0
if a == 1:
    print('Yes! a = 1')
else:
    print('Sorry! a is not equal to 1')

# Zodiac Sign
sagitarius = "Good Man! " 
pisces = "Scientist"
scorpio = 'Hard Working!'
print('1. Sagitarius\n'+'2. Piecies\n'+'3. Scorpio')
user_input = input('Enter any number from the above list!')
if user_input == '1':
    print(sagitarius)
elif user_input == '2':
    print(pisces)
elif user_input == '3':
    print(scorpio)
else:
    print('Please choose the correct zodiac sign from the given list')