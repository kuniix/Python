#exercicio 1:
# contador = 10
# for i in range(10):
#     contador -= 1
#     print(contador)
# print("Beep")

#exercicio 2:
numero = int(input("Digite um numero: "))
numero_multiplicador = int(input("Quer fazer a tabuada até qual numerando:"))

for i in range(numero_multiplicador):
    print(f"{numero} x {i+1} = {numero * (i+1)}")