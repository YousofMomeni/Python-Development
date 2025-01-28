num = []
num2 = []

for i in range(5):
    x = int(input('Enter a number: '))
    num.append(x)

print('old list : ',num)

for i in range(len(num)):
    if num[i]%2 == 0 :
        num2.append(num[i])
print('new list : ',num2)
