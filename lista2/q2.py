try:

	def Porcentagem(valor):

		return valor * 0.7

	x = float(input("Mostre na tela o valor em real (R$): "))


	print("70%c de %f � %f." % ("%", x, Porcentagem(x)))

except:

	print("Um valor real n�o foi inserido.")