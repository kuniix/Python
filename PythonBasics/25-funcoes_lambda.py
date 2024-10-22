#Função de potencia
power = lambda num: num**2

#função de verificação de par
pair = lambda x: x % 2 == 0

#funçao de divisão
div_num = lambda x, y : x * y

reverse = lambda s: s[::-1]

print(power(5))
print(power(10))
print(pair(10))
print(pair(31))
print(div_num(10,5))
print(div_num(31,18))
print(reverse("Django"))