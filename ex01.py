# 1) Desenvolva um programa que receba do usuário um valor numérico inteiro x e retorne como
# saída o resultado da seguinte fórmula: x² + 10x - 5

x = int(input('O valor de x é: '))

resultado = (x * x) + 10 * x - 5
print(f'O resultado da equação é {resultado:.2f}')