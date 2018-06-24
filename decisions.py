a,b = 1,2

# single condition
if a == 1:
    print('a is equal to 1')
else:
    print('a is not equal to 1')

# multiple condition
if a < b and b > a:
    print('success')
else:
    print('False')

if a < b or b > a:
    print('success')
else:
    print('False')