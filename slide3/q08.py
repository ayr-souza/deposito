print("--- Loja Mamão com Açúcar ---\n")

try:

	v = float(input("Forneça o valor da compra: "))

	print("O produto deve ser pago em cinco prestações (sem juros) de R$ %.3f." % (v / 5))

except:

	print("Não foi fornecido um valor real.")