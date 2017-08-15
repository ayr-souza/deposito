try:

	a = float(input("Forneça dois números: "))
	b = float(input())

	print("O produto entre %.3f e %.3f é %.3f." % (a, b, a * b))

except:

	print("Você não forneceu dois valores reais.")