day = input()
price = float(input())
option = input()    
productName = input()


if day in ('seg', 'ter', 'qua') and option == 'ouro':
    print(f'O preco do produto {productName} no dia {day} eh {price/2:.2f}')

elif day in ('qui', 'sex') and price >= 10 and price <=100:
    print(f'O preco do produto {productName} no dia {day} eh {price/3:.2f}')
       
elif day == 'sab' and option == 'prata':
    print(f'O preco do produto {productName} no dia {day} eh {price*3:.2f}')
else:
    print(f'O preco do produto {productName} no dia {day} eh {price*2:.2f}')