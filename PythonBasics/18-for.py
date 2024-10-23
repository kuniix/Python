"""game_list = ["DBSZ", "POE 2", "LOL", "VALORANT"]

for index in game_list:
    print(index)

print (f"================")

#2 quando a condição for atendida, o loop será encerrado
for index in game_list:
    if index == "LOL":
        break
    print(index)
    
    
print (f"================")


#3 - quando a condição for atendida, vai até a proxima iteração
for index in game_list:
    if index == "LOL":
        continue
    print(index)

print (f"================")


#4 calcular
game_name = input("Digite o nome do jogo\n")
game_rating = (int(input("Quantas avaliações quer fazer no jogo?\n")))

sum = 0
for i in (game_list):
    nota = float(input("Qual a nota:\n"))
    sum += nota

media = sum / game_rating

print(f"A média das notas do jogo {game_name} é {media}")"""
"""

lista = [2,3,4,5,6,7,10,6,89,6,5,8]
palavra = "Jureg n da silvaior"

for letra in palavra:
    print(letra)"""

"""for numero in range(1, 11):
    print(numero)"""
"""
nome = input("Digite seu nome: ")
for x in range(10):
    print(f"{x+1} : {nome}")
"""
#range(valor_inicial, valor_final, incremento)
"""for x in range(20,0,-2):
    print(x)"""
"""
pedras = ("Rubi","Esmeral","Quartzo","Safira","Diamante","Turmalina")

for pedra in pedras:
    if pedra != "Quartzo":
        print(f"{pedra}")

for pedra in pedras:
    if pedra == "Quartzo":
        continue
    print(f"{pedra}")"""