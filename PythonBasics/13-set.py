game_set = {"fifa 23", "skyrim", "diablo 4", "epic seven", "summoners wars", "jigoku parade"}
print(game_set)

#1 buscar o tamanho do set
print(len((game_set)))

#2 True e 1 são considerados o mesmo valor (somente no set?)
example_set = {"fifa 23", True, 1, 90.50}
print(example_set)

#3 adicionar item de outro set
game_set.update(example_set)
print(game_set)

#4 remover item
game_set.remove(True)
game_set.remove(90.50)

#5 nao possibilita recuperar valores via fatiamento ou slice
