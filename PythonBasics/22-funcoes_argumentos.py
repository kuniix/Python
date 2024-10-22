#1 - criar uma função que recebe dois argumentos: o primeiro nome e o segundo nome
def full_name(first_name, last_name):
    print(f"O nome é {first_name} e o sobrenome {last_name}")

full_name(10,11)

#2 - criar um função que recebe 2 valores e faça operação de soma
def soma(primeiro_valor, segundo_valor):
    return primeiro_valor + segundo_valor

print(f"{soma(10, 5)}")

#3 argumentos default numa função
def address(country = "Brasil"):
    return country

print(f"{address("Japão")}")

#4 - avaliação de jogo:
def rating_game(qtd_rating):
    game_name = input("Nome do jogo: ")
    sum = 0
    for i in range(qtd_rating):
        note = float(input("Nota do jogo: "))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é {sum / qtd_rating}")
rating = int(input("Quantas avaliaçoes: "))
rating_game(rating)