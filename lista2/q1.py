def Mensagem():

	x = 10
	y = 1
	x -= 1
	y += 2
	x = x - 1
	y = y + 2
	x = x - 1
	y = y + 2

	return "\'x\' = " + str(x) + " e \'y\' = " + str(y)

print(Mensagem())

def Funcao(b):

	a = (b * 2)
	b = b + 5
	c = a - b

	return "a = %d; b = %d; c = %d" % (a, b, c)

print(Funcao(0))

print(Funcao(5))

print(Funcao(10))

print(Funcao(15))

print(Funcao(20))