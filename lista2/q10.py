def triplo(x):

	return x * 3

try:

	x = float(input("Insira um número real: "))

	print("O triplo de %f é %f." % (x, triplo(x)))

except:

	print("Um número real não foi inserido.")