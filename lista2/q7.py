def expr(x, y):

	return (x + y) / (x - y)

try:

	x = float(input("Forne�a dois valores reais: "))
	y = float(input())

	print(expr(x, y))

except:

	print("Voc� n�o forneceu valores reais.")