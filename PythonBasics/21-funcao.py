def welcome():
    print("Hello world!")

welcome()

#2 função para somar dois numeros
def sum():
    return 5 + 4

print(sum())


#3 função para cadastrar um game
def create_game():
    name = input("Digite o nome do jogo: ")
    year_launch = int(input("Ano de lançamento: "))
    game_price = float(input("Preço: "))
    note_rating = float(input("Nota: "))
    print(f"{name} - R${game_price}")

create_game()