games_list = ["DBSZ", "POE 2 ", "DIABLO 4", "Minecraft"]

#1 - tamanho da lista
print(len(games_list))

#2 - recuperar um item da lista pelo indice
print(games_list.index("Minecraft"))

#3 - adicionar um item ao final da lista
games_list.append("GTA 6")
print(games_list)

#4 - ordenar a lista
games_list.sort()
print(games_list)
games_list.reverse()
print(games_list)

#6 - copiar itens de uma lista pra outra
game_reset = games_list.copy()
game_reset.remove("GTA 6")
print(game_reset)