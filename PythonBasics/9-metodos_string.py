game_name = "Dragon ball sparking zero"
game_description = """
    Dragon Ball Sparking Zero is a 2D action-adventure game developed by Bandai Namco Entertainment and published by Nintendo for the Nintendo 64. The game was released in Japan on October 20, 2000, and in North America on November 11, 2000. The game was released for the Nintendo 64 on November 19, 2000, and for the GameCube on February 18, 2001.

    Dragon Ball Sparking Zero is set in the fictional world of Dragon Ball Z, a series of superhero games created by Namco and published by Sony Computer Entertainment. The game follows the story of Goku, a young and powerful fighter, who must protect the world from the evil forces of the Dragon Balls.
"""

print(game_name.upper()) #Retorna string em maiusculo
print(game_name.lower()) #retorna string em minususculo
print(game_name.capitalize()) #retorna string com a primeira letra em maiusculo
print(game_name.title()) #retorna string com a primeira letra em maiusculo
print(game_name.center(50, '-')) #centraliza a string preenchendo as laterais
print(game_name.find("a")) #retorna a primeira posição que o caracterere se encontra
print(game_name.count("o")) #conta quantas vezes o caractere apareceu
print(game_name.replace("zero", "Z")) #susbtitui o primeiro valor pelo segundo
print(game_description.split(',')) #separa a string com base no caractere