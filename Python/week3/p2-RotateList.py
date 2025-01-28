num = []

for i in range(5):
    x = int(input('Enter a number: '))
    num.append(x)

print('old list: ',num)
rotate = int(input('enter rotate: '))

for i in range(rotate):
    y = num[0]
    num.pop(0)
    num.append(y)

print('new list: ',num)
