num1 = float(input("Digite o número 1\n"))
num2 = float(input("digite o número 2\n"))
operation = input("Digite a operação a ser realizada (+ - / *\n)")

if operation == "+":
    print(f"Operação escolida soma:")
    print(f"A soma entre {num1} e {num2} é {num1 + num2}")
elif operation == "-":
    print(f"Operação escolida subtração:")
    print(f"A subtração entre {num1} e {num2} é {num1 - num2}")
elif operation == "/":
    if num2 != 0:
        print(f"Operação escolida divisão:")
        print(f"A divisão entre {num1} e {num2} é {num1 / num2:.2f}")
    else:
        print("Não é possível realizar a divisão por zero.")
elif operation == "*":
    print(f"Operação escolida multiplicação:")
    print(f"A multiplicação entre {num1} e {num2} é {num1 * num2}")
else:
    print("Operação inválida.")
