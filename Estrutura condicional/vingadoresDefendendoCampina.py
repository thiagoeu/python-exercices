listaHerois = ['Homem de Ferro', 'Hulk', 'Capitão América', 'Thor', 'Gavião Arqueiro', 'Viúva Negra']
vingador = input()

if vingador not in listaHerois:
    print('Vingador Inválido')

else:
    poder = input()
    energia = int(input())

    hferro = ['Homem de Ferro', 'Armadura de Ferro']
    hulk = ['Hulk', 'Força Bruta']
    camerica = ['Capitão América', 'Escudo']
    thor = ['Thor', 'Martelo']
    arqueiro = ['Gavião Arqueiro', 'Arco e Flecha']
    viuva = ['Viúva Negra', 'Inteligência']

    listaUsuario = [vingador, poder]




    if listaUsuario == hferro:
        if energia >= 10:
            print(f'{vingador} conseguiu derrotar Thanos')
        else:
            print(f'{vingador} NAO conseguiu derrotar Thanos, chamem outro Vingador')

    elif listaUsuario == hulk:
        if energia >= 5:
            print(f'{vingador} conseguiu derrotar Thanos')
        else:
            print(f'{vingador} NAO conseguiu derrotar Thanos, chamem outro Vingador')

    elif listaUsuario == camerica:
        if energia >= 7:
            print(f'{vingador} conseguiu derrotar Thanos')
        else:
            print(f'{vingador} NAO conseguiu derrotar Thanos, chamem outro Vingador') 
           
    elif listaUsuario == thor:
        if energia >= 4:
            print(f'{vingador} conseguiu derrotar Thanos')
        else:
            print(f'{vingador} NAO conseguiu derrotar Thanos, chamem outro Vingador')    

    elif listaUsuario == arqueiro:  
        if energia >= 12:
            print(f'{vingador} conseguiu derrotar Thanos')
        else:
            print(f'{vingador} NAO conseguiu derrotar Thanos, chamem outro Vingador')    

    elif listaUsuario == viuva:
        if energia >= 20:
            print(f'{vingador} conseguiu derrotar Thanos')
        else:
            print(f'{vingador} NAO conseguiu derrotar Thanos, chamem outro Vingador')    

    elif listaUsuario[0] in listaHerois:
        if poder == hulk[1]:
            print(f'{vingador} NAO conseguiu derrotar Thanos')
            print(f'Esse é o poder do {hulk[0]}') 
        elif poder == hferro[1]:
            print(f'{vingador} NAO conseguiu derrotar Thanos')
            print(f'Esse é o poder do {hferro[0]}')               
        elif poder == camerica[1]:
            print(f'{vingador} NAO conseguiu derrotar Thanos')
            print(f'Esse é o poder do {camerica[0]}')
        elif poder == thor[1]:
            print(f'{vingador} NAO conseguiu derrotar Thanos')
            print(f'Esse é o poder do {thor[0]}')
        elif poder == arqueiro[1]:
            print(f'{vingador} NAO conseguiu derrotar Thanos')
            print(f'Esse é o poder do {arqueiro[0]}')
        elif poder == viuva[1]:
            print(f'{vingador} NAO conseguiu derrotar Thanos')
            print(f'Esse é o poder do {viuva[0]}')  

            
        
