num = []
num2 = []

for i in range(5):
    x = int(input('Enter a number: '))
    num.append(x)

for i in range(len(num)):
    if not num[i] in num2:
        num2.append(num[i])

print('old list: ',num)
print('new list: ',num2)

