valor = int(input('Qual valor você quer sacar? R$'))
total = valor
dinheiro = 50
totaldinheiro = 0
while True:
    if total >= dinheiro:
        total -= dinheiro
        totaldinheiro += 1
    else:
        if totaldinheiro > 0:
            print(f'Total de {totaldinheiro} cédulas de R${dinheiro}')
        if dinheiro == 50:
            dinheiro = 20
        elif dinheiro == 20:
            dinheiro = 10
        elif dinheiro == 10:
            dinheiro = 1
        totaldinheiro = 0
        if total == 0:
            break
print('-' * 40)
print('Programa finalizado')
