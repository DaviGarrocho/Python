import math

co = float(input('fale o cateto oposto de um triangulo retangulo: '))
ca = float(input('fale o cateto adjacente dele agora: '))
h2 = (math.pow(co, 2)) + (math.pow(ca, 2))
h = math.sqrt(h2)
hi = math.hypot(co, ca)
print('O comprimento da hipotenusa deste triangulo retangulo e igual a {:.2f}'.format(hi))
