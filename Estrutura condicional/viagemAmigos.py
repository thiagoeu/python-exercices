pessoas = int(input())
cidade = input()
quartos = int(input())


pipa2 = 600+(pessoas*75)
pipa3 = 900+(pessoas*75)

fortaleza3 = 950+(pessoas*60)
fortaleza4 = 1120+(pessoas*60)

if cidade.lower() == 'pipa':
    if quartos == 2:
        print(f'{pipa2:.2f}')
        print (f'{(pipa2/pessoas):.2f}')
    elif quartos == 3:
        print(f'{pipa3:.2f}')
        print (f'{(pipa3/pessoas):.2f}')

elif cidade.lower() == 'fortaleza':
    if quartos == 3:
        print(f'{fortaleza3:.2f}')
        print(f'{(fortaleza3/pessoas):.2f}')
    if quartos == 4:
        print(f'{fortaleza4:.2f}')
        print(f'{(fortaleza4/pessoas):.2f}')
        