password = 'python123'
x = 3
user = input('Enter your password: ')

if user == password:
    print('login')
else:
    print('error : try again')
    x -= 1
    print('Opportunity :',x)
    user = input('Enter your password: ')
    if user == password:
        print('login')
    else:
        print('error : try again')
        x -= 1
        print('Opportunity :',x)
        user = input('Enter your password: ')
        if user == password:
            print('login')
        else:
            print('error')