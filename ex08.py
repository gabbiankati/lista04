# 8) Uma loja está realizando um levantamento a respeito das pendências financeiras dos seus
# clientes. A ideia é levantar o percentual de clientes que se enquadram em cada uma das
# seguintes situações:
# • Clientes isentos de pendências
# • Clientes com parcelas em dia e
# • Clientes com parcelas em atraso.
# Para isto, desenvolva um programa que receba do usuário o número de clientes em cada uma
# destas situações, e retorne como saída para o usuário o percentual de clientes que se enquadra
# em cada uma das situações.

isentos = int(input("Digite o número de clientes isentos de pendências: "))
em_dia = int(input("Digite o número de clientes com parcelas em dia: "))
em_atraso = int(input("Digite o número de clientes com parcelas em atraso: "))

total = isentos + em_dia + em_atraso

percentisento = (isentos / total) * 100
percentdia = (em_dia / total) * 100
percentatraso = (em_atraso / total) * 100

print("Percentual de clientes isentos de pendências:", percent_isentos, "%")
print("Percentual de clientes com parcelas em dia:", percent_em_dia, "%")
print("Percentual de clientes com parcelas em atraso:", percent_em_atraso, "%")

