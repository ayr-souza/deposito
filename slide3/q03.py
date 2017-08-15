try:

	x = int(input("Forneça um número inteiro: "))

	print("O antecessor de %d é %d. O seu sucessor, %d." % (x, x - 1, x + 1))

except:

	print("Você não forneceu um valor inteiro.")