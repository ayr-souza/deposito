try:

	c = float(input("Forneça o valor de custo do produto em reais (em R$): "))
	p = float(input("Forneça o valor do percentual de aumento: "))
	p /= 100 

	print("O preço de venda do produto deve ser R$ %.2f." % (c + (c * p)))

except:

	print("Não foram fornecidos valores reais.")