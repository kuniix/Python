num1 = int(input("Digite um número\n"))
num2 = int(input("Digite um número\n"))

#Aritiméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"O resto da divisão entre {num1} e {num2} é {mod}")
print(f"O expoente entre {num1} e {num2} é {exp}")

#Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2


print(equal)
print(smaller)

#Comparação
num1 += num2
num1 -= num2
num1 /= num2
num1 *= num2
num1 **= num2
num1 %= num2
