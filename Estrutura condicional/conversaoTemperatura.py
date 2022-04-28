escalaTemp = input()

Temp = float(input())


if  escalaTemp == 'C':
    if Temp >= -273:
        print(f'{(Temp * 9/5) + 32:.2f} F')
        print(f'{Temp+273.15:.2f} K')
    else:
        print("Valor de temperatura abaixo do minimo")
        
if escalaTemp == 'F':
    if Temp >= -459.67:
        print(f'{(Temp-32)*5/9:.2f} C')
        print(f'{(Temp- 32)*5/9+273.15:.2f} K')
    else:
        print("Valor de temperatura abaixo do minimo")

if escalaTemp == 'K':
    if Temp >= 0.0:
        print(f'{Temp-273.15:.2f} C')
        print(f'{(Temp-273.15)*9/5+32:.2f} F')       
    else:
        print("Valor de temperatura abaixo do minimo")   