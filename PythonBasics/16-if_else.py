name = input("Digite o nome do jogo\n")
year_launch = int(input("Em que ano foi lançado?\n"))
classification = float(input("qual a nota do jogo\n"))

if classification >= 8:
    print(f"Recomendado para jogar")
    
else:
    print(f"Não recomendado para jogar")