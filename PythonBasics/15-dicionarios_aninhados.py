import pprint

games_dict = {
    "Dragon ball sparking zero": {
        "game_price": 299.99,
        "game_genre": "fighing game",
        "year_launch": 2024
    },
    "Megaman x4": {
        "game_price": 37.99,
        "game_genre": ["2d", "platform"],
        "year_launch": 2004
    },
    "Throne and Liberty": {
        "game_price": 0,
        "game_genre": "mmorpg",
        "year_launch": 2020
    }
    
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(games_dict)

#1 buscar informção dentro do dicionario aninhado
print(games_dict["Megaman x4"]["game_price"])

#2 adicionar um novo item
games_dict["Megaman x4"]["players"] = 20
print(games_dict["Megaman x4"]["players"])

#3 excluir um dicionario
del games_dict["Megaman x4"]
pp.pprint(games_dict)