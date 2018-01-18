def conversor(minutos):

	horas = minutos // 60
	mins = minutos % 60

	return horas, minutoreturn

try: 

	m = int(input("Forneça o valor em minutos: "))

	horas, minutoreturn = conversor(m)

	print("%d minutos é igual a %d horas e %d minutos." % (m, horas, minutoreturn))

except:

	print("Um valor inteiro não foi inserido.")  