import random
al1 = str(input('1º aluno: '))
al2 = str(input('2º aluno: '))
al3 = str(input('3º aluno: '))
al4 = str(input('4º aluno: '))
al5 = str(input('5º aluno: '))
al6 = str(input('6º aluno: '))
al7 = str(input('7º aluno: '))
al8 = str(input('8º aluno: '))
al9 = str(input('9º aluno: '))
al10 = str(input('10º aluno: '))
lista = [al1,al2,al3,al4,al5,al6,al7,al8,al9,al10]
print('o aluno que vai limpar o quadro e o/a {}'.format(random.choice(lista)))