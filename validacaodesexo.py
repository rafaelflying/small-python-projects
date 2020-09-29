sexo = str(input('informe seu sex: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, digite seu sexo: '
                     '[M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))


