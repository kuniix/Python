"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos quereremos ter numa função
- Os argumentos são passados como uma tupla


**kwargs - Além dos valores podemos tambem passar as respectivas chaves para cada argumento
- Os argumentos são passados como um dicionario
"""

def sum(*num):
    sum_total = 0
    for i in num:
        sum_total += i
    print(f"Soma é: {sum_total}")

sum(4,10,30)

#2 - apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


print("Cursos  =-=-=-==-==-=-==-=-=-=-=--=--=")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Java", category="Backend", level="Avançado")
presentation(name="SQL", category="Banco de dados")