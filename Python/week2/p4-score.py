score = int(input('Enter your score:'))

if score:
    if 100 <= score >= 0 :
        if score >= 90:
            print('excellent')
        elif 90 > score <= 70:
            print('good')
        elif 70 > score <= 50:
            print('Needs effort')
        else:
            print('You have been rejected')
    else:
        print('error')
else:
    print('error')