lvl = int(input())


if lvl >= 1 and lvl <= 20:
    print(f'Potencia de : {20+lvl**3} W')
elif lvl >= 21 and lvl <=40:
    print(f'Potencia de : {8000+(lvl-10)**2} W')
elif lvl >= 41 and lvl <= 60:
    print(f'Potencia de : {9000+5*lvl} W')
elif lvl >= 61 and lvl <= 80:
    print(f'Potencia de : {9300+2*lvl} W')
elif lvl >= 81 and lvl <= 100:
    print(f'Potencia de : {9500+lvl} W')   