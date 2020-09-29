preco = float(input('preço das compras: R$'))
print('''Formas de pagmento
1 - à vista dinheiro/cheque
2 - à vista cartão
3 - 2x no cartão
4 - 3x ou mais no cartão''')
opcao = int(input('qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco *0.20)
    totparc = int(input('quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em 2x de R${:.2f} '
          'COM JUROS'.format(totparc, parcela))
else:
    total = preco
    print('opção inválida de pagamento. Tente denovo!')
print('Sua compra de R${:.2f} vai custar R${:.2f} '
      'no final'.format(preco, total))

