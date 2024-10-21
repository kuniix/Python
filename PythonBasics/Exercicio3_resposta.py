#Exercicio 1
"""distancia = float(input("Qual a distancia da corrida: "))
passagem = 0.50

if distancia > 200:
    passagem = 0.35
    preco = passagem * distancia
    print(f"A distancia da corrida é de {distancia}km, por isso o valor por km é: {passagem}. O valor da corrida ao total é de : R${preco:.2f}")
else:
    preco = passagem * distancia
    print(f"A distancia da corrida é de {distancia}km, por isso o valor por km é: R${passagem}. O valor da corrida ao total é de : R${preco:.2f}")
    """
#Exercicio 2
salario = float(input("Salario do funcionario: "))
if salario > 1250:
    print(f"O salario é superior a R$1250 portanto o aumento será de 10%")
    aumento = salario * (10 / 100)
    print(f"O aumento é de R${aumento}, portanto o salario fechou em R${salario + aumento}")
else:
    print(f"O salario é inferior a R$1250, portanto o aumento será de 15%")
    aumento = salario * (15 / 100)
    print(f"O aumento é de R${aumento}, portanto o salario fechou em {salario + aumento}")