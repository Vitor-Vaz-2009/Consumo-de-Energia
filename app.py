#Entrada de dados
print ("=== Calculadora de Consumo de Energia ===")
aparelho = input("Digite o nome do aparelho: ")
potencia_do_aparelho = float(input("Digite a potência do aparelho em watts (W): "))
horas_de_uso_diario = float(input("Digite o número de horas que o aparelho é usado por dia: "))

#Calculos
consumo = potencia_do_aparelho * horas_de_uso_diario * 30 / 1000
valor_kwh = float(input("Digite o preço do kWh em sua região: "))
custo_mensal = consumo * valor_kwh

#Saída de dados
print("\n=== Resultado ===")
print(f"O consumo mensal do {aparelho} é de {consumo:.2f} kWh/mês.")
print(f"O custo mensal para usar o {aparelho} é de R$ {custo_mensal:.2f}.")
