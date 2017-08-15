try:

	x = float(input("Forneça um número: "))

	print("O triplo de %.3f é %.3f." % (x, x * 3))

except:

	print("Você não forneceu um valor real.")