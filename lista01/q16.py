valor = float(input("Forneça os valores do valor, da taxa e do tempo, respectivamente: "))
taxa = float(input())
tempo = float(input())

prestacao = valor + (valor * (taxa / 100) * tempo)

print("O valor da prestação é", prestacao, end = ".\n")