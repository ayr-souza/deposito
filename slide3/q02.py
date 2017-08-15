try:

	v = float(input("Forneça um valor em reais (R$): "))

	print("70%c de R$ %.2f é R$ %.2f." % ("%", v, v * 0.7))

except:

	print("Você não forneceu um valor real.")