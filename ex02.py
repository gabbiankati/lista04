# 2) Considere que para um consórcio sabe-se o número total de prestações, a quantidade de
# prestações pagas e o valor da prestação. Escreva um programa que determine o valor total pago
# pelo consorciado e o saldo devedor.

numeroPrestacao = float(input('Número de prestações: '))
valorPrestacao = float(input('Valor de prestações: '))
prestacaoPaga = float(input('Prestações pagas: '))

valorPago = prestacaoPaga * valorPrestacao
prestacoesRestantes = numeroPrestacao - prestacaoPaga
saldoDevedor = valorPrestacao * prestacoesRestantes

print(f'O valor total que já foi pago é de: {valorPago:.2f}, e o saldo devedor é de: {saldoDevedor:.2f}')





