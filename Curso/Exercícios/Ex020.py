import random
al1 = str(input('fale o nome de um aluno: '))
al2 = str(input('fale o nome de outro aluno: '))
al3 = str(input('fale o nome do outro aluno: '))
al4 = str(input('fale o nome do ultimo: '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('a ordem sera {}'.format(lista))