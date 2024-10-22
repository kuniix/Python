def factorial(num):
    if num == 1:
        return 1
    else:
        return(num * factorial(num -1))

number = int(input("Digite o número para o fatorial"))
print(f"O fatorial de {number} é {factorial(number)}")

#soma total de um numero

def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))
num = int(input("Digite um número para soma: "))
print(f"A soma total do {num} é: {total_sum(num)}")
    

