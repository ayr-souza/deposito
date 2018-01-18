def resultado(k):

	return k / 3.6

try:

	k = float(input("Insira um valor correspondente em km/h: "))

	print("%f km/h equivale a %f m/s." % (k, resultado(k)))

except:

	print("Você não inseriu um valor real.")