def triplo(x):

	return x * 3

try:

	x = float(input("Insira um n�mero real: "))

	print("O triplo de %f � %f." % (x, triplo(x)))

except:

	print("Um n�mero real n�o foi inserido.")