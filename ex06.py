# 04) Suponha que um caixa disponha apenas de cédulas de R$ 100, 10 e 1. Escreva um programa
# para ler o valor de uma conta e o valor fornecido pelo usuário para pagar essa conta, e calcule e
# troco. Calcular e mostrar a quantidade de cada tipo de cédula que o caixa deve fornecer como
# troco. Mostrar, também o valor da compra e do troco.

conta = float(input("Digite o valor da conta: R$ "))
fornecido = float(input("Digite o valor fornecido pelo usuário: R$"))

troco = fornecido - conta

cedula100 = int(troco / 100)
troco = fornecido - conta
cedula10 = int(troco / 10)
cedula1 = int(troco)

print("Valor da compra: R$", conta)
print("Valor fornecido pelo usuário: R$", fornecido)
print("Valor do troco: R$", troco)
print("Quantidade de cédulas de R$100:", cedula100)
print("Quantidade de cédulas de R$10:", cedula10)
print("Quantidade de cédulas de R$1:", cedula1)
