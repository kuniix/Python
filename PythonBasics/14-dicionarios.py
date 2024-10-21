game_dbsz = {
    "name": "Dragon Ball Sparking Zero",
    "year_launch": 2024,
    "game_price": 399.99,
    "steam_classification": 10,
    "genre": ["Fighting game", "online"]
}

print(game_dbsz)
print(len(game_dbsz))
print(type(game_dbsz))


#1 recuperar um elemento do dicionario
print(game_dbsz["genre"])
print(game_dbsz.get("steam_classification"))

#2 buscar apenas as chaves do dicionario
print(game_dbsz.keys())

#3 buscar valores do dicionario
print(game_dbsz.values())

#4 buscar itens do dicionario com chave e valores  || isso aqui retorna chave e valor em tuplas
print(game_dbsz.items())

#5 adicionar um novo item ao dicionario
game_dbsz["discount_avaliable"] = False
print(game_dbsz)

#6 atualizar itens no dicionario
game_dbsz.update({"discount_avaliable" : True})
print(game_dbsz)

#7 remover um item do dicionario
game_dbsz.pop("steam_classification")
print(game_dbsz)