while True:
    num = []
    x = int(input('Enter the number of scores: '))
    
    for i in range(x):
        y = int(input('Enter a number: '))
        num.append(y)

    students = x
    total = sum(num)
    average = total / students

    print('student:' , students )
    print('sum:' , total )
    print('average:' , average )

    q = input('Do you want to do it again?(y/n) ')
    if q == 'n' :
        break