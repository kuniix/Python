game_name = "Dragon Ball Sparking Zero"
game_description = """
    Dragon Ball Sparking Zero is a 2D action-adventure game developed by Capcom and published by Nintendo for the PlayStation 4 and GameCube consoles.
    The game revolves around a young boy named Goku, who embarks on a journey to save the world from an evil dragon using various characters and weapons.
"""
#String[inicio:fim] - incice começa na posição 0 \ indice final -1

#1 busque toda string a partir da primeira posição
print(game_name[0:])

#2 busque toda string até a ultima posição
print(game_name[:6])

#3 busque toda string da terceira até a ultima posição
print(game_name[2:])

"""
    string[inicio:fim:passo] - indice começa na posição 0 | indice final -1
    passo - determina o incremento (padrão é 1)
    """

#4 busque toda string de 2 em 2 caracteres
print(game_name[::2])

#5 busque toda string nos indices impares
print(game_name[1::2])

#6 inverter uma string de tras pra frente
print(game_name[::-1])
