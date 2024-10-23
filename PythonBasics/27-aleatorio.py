import random
"""
print(f"Gerar cinco números aleatorios entre 1 e 50: \n")
for i in range(5):
    numero = random.randint(1,50)
    print(f"Número gerado: {numero}")"""

"""valor = random.random()
print(f"Número gerado: {round(valor * 10, 2)}")

valor = random.uniform(1,100)
print(F"Número: {round(valor, 4)}")"""

lista = [2,5,6,7,3,1,2,3,5,4,6,80,47,6,6,80,40,6,32,321,3156,654,432,423,452151,2412,412,1425]
#numero = random.choice(lista)
#print(numero)

#numero = random.sample(lista, 3)
#print(numero)

print(f"Exibir a lista original:\n{lista}")

print(f"Embaralhar a lista e exibi-la")
lista_alterada = random.shuffle(lista)
print(lista)