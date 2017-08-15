try:

	a = float(input("Forneça dois números: "))
	b = float(input())

	print("A soma entre %.3f e %.3f é %.3f.\nA subtração entre %.3f e %.3f é %.3f.\nA multiplicação entre %.3f e %.3f é %.3f.\nA divisão entre %.3f e %.3f é %.3f." % (a, b, a + b, a, b, a - b, a, b, a * b, a, b, a / b))

except:

	print("Você não forneceu dois valores reais.")