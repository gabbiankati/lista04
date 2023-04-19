# 03) Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro
# quadrado de área deve-se usar 18 watts de potência. Desenvolva um programa que receba as
# dimensões de dois lados de uma casa (em metros), calcule a área da casa (A = lado * lado), e
# mostre quantos watts serão necessários para iluminar corretamente esta casa.

lado1 = float(input("Digite a medida do primeiro lado da casa em metros: "))
lado2 = float(input("Digite a medida do segundo lado da casa em metros: "))


area = lado1 * lado2
potencia = area * 18

print("Para iluminar corretamente uma casa com dimensões de", lado1, "m x", lado2, "m, serão necessários", potencia, "watts de potência.")