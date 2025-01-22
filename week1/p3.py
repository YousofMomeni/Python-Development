model = int(input('miladi(1) or shamsi(2)'))
age = int(input('Enter your year of birth: '))

if model == 1:
    print(2024-age)
elif model == 2:
    print(1403-age)
else :
    print('error')