name = input("Digite o nome do jogo:\n")
year_launch = int(input("Digite o ano de lançamento do jogo:\n"))
game_price = float(input("Digite o preço do jogo:\n"))
plan_included = bool(input("Está incluso no jogo:\n"))

print("Dados do jogo")
print("=====================")

#Alternativa 1
'''
print("Nome do jogo:",name)
print("=====================")
print("Ano de lançamento do jogo:",year_launch)
print("=====================")
print("Preço do jogo:",game_price)
print("=====================")
print("Está incluso no plano:", plan_included)'''

#Alternativa 2
#print("Nome do jogo:", name,"\nAno de lançamento do jogo:", year_launch, "\nPreço do jogo:", game_price, "\nEstá incluso no plano", plan_included)

#Alternativa 3
print(f"Nome do jogo: {name} \nAno de lançamento do jogo: {year_launch} \nPreço do jogo: {game_price} \nEstá incluso no plano? {plan_included}")