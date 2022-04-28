idade = int(input())
jogo = input()



if idade < 0:
    print('Idade invalida.')

if idade >= 21:
    if jogo == "azar" or jogo == 'mmorpg' or jogo == 'casual' or jogo == 'moba':
        print('Pode entrar!')
    elif jogo != ('azar', 'mmoprg', 'casual', 'moba'):
        print('Jogo invalido.')    
        
if idade >= 14 and idade < 21:
    if jogo == 'mmorpg' or jogo == 'casual' or jogo == 'moba':
        print('Pode entrar!')
    elif jogo == 'azar':
        print ('Volte daqui há alguns anos.')    
    elif jogo != ('azar', 'mmoprg', 'casual', 'moba'):
        print('Jogo invalido.')    

if idade >= 10 and idade < 14:
    if jogo == 'moba' or jogo == 'casual':
        print('Pode entrar!')
    elif jogo == 'azar' or jogo == 'mmorpg':
        print ('Volte daqui há alguns anos.')
    elif jogo != ('azar', 'mmoprg', 'casual', 'moba'):
        print('Jogo invalido.')
if idade < 10 and idade > 0:
    if jogo == 'casual':
        print('Pode entrar!')
    elif jogo == 'azar' or jogo == 'mmorpg' or jogo == 'moba':
        print ('Volte daqui há alguns anos.')
    elif jogo != ('azar', 'mmoprg', 'casual', 'moba'):
        print('Jogo invalido.')