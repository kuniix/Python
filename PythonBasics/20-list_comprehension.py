#1 lista de valores de 0 a 10 que sejam menor do que 4
# for  in range (10):
#     if i < 4:
#         print(i)

list_numbers = [i for i in range(10) if i < 4] 
print(list_numbers)

games_list = ["POE 2", "VALORANT", "LOL", "AION"]

#2 jOGOS QUE POSSUAM A LETRA A
new_list =  [i for i in games_list if "A" in i]
print(new_list)

#3 JOGOS QUE EU ZEREI
game_finished = [i for i in games_list if i != "POE 2"]
print(game_finished)