def net(n, e, t):

	print("\n\nNome: %s.\nEndere�o: %s.\nTelefone: %s." % (n, e, t))

try:

	n, e, t = input("Forne�a:\n\nNome: "), input("Endere�o: "), input("Telefone: ")

	net(n, e, t)

except:

	print("Voc� n�o forneceu os dados.")