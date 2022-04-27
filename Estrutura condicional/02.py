livros = int(input())
alunos = int(input())

media = (alunos/livros)

if media > 18:
    print("D")

elif media >= 13 and media <= 18:
    print("C")

elif media >= 9 and media <= 12:
    print("B")

else:
    print("A")