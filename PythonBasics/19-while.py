"""game_name = input("Digite o nome do jogo: ")
qtd_rating =0
total_rating = 0
rating = 0
avarage = 0

while(rating != -1):
    rating = float(input("Informe a nota do jogo: "))
    if rating == -1:
        break
    else:
        qtd_rating += 1
        total_rating += rating
        avarage = total_rating / qtd_rating

print(f"A média das avaliaçoes do jogo {game_name} é {avarage:.2f}")
"""

"""numero = 1
while numero <= 10:
    print(f"{numero}")
    numero +=1"""
    
nome = None
while True:
    print(f"Digite seu nome, ou x para parar.")
    nome = input()
    if nome == "x" or nome == "X":
        break

    print(f"Bem vindo, {nome}")