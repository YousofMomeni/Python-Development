Product = [
    {'name':'asus' ,'model':'tuf' ,'price':'70'},
    {'name':'lenovo' ,'model':'z' ,'price':'26'},
    {'name':'hp' ,'model':'omen' ,'price':'75'}
]

def append():
    name = input('Enter name product: ')
    model = input(f'Enter model {name}: ')
    price = input(f'Enter price {name} {model}: ')
    new_product = {'name': name , 'model': model , 'price': price }
    Product.append(new_product)
    print(Product[-1])


def Search():
    Search = input('Enter procuct: ')
    for i in Product:
        if i['name'] == Search :
            print('Product found: ',i)
            return
        print('Product not found!')
        return

def remove():
        Search = input('Enter procuct: ')
        for i in Product:
            if i['name'] == Search :
                Product.remove(i)
                print('removed')
                return
        print('Product not found!')
        return


def replace():
    search = input('Enter procuct: ')
    for index,i in enumerate(Product):
        if i['name'] == search :
            Product[index]['name'] = input('Enter name product: ')
            Product[index]['model'] = input('Enter model product: ')
            Product[index]['price'] = input('Enter price product: ')
            print('replace',Product[index])
            return
        
def view():
    for i in Product:
        print(i)




        
print('********************************************************')
print('*                  View List : 1                       *')
print('*                  Add List : 2                        *')
print('*                  Search List : 3                     *')
print('*                  Remove List : 4                     *')
print('*                  Replace List : 5                    *')
print('********************************************************')

while True:

    x = int(input('Enter number: '))
    if x == 1:
        view()
    elif x == 2:
        append()
    elif x == 3:
        Search()
    elif x == 4:
        remove()
    elif x == 5:
        replace()
    else:
        print('Error!')
