num = int(input('digite um número: '))
total = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} for divisível {} vezes'.format(num, total))
if total == 2:
    print('é primo')
else:
    print('não é primo')
