'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''
print('TABUADA')
print('-*' * 23)
while True:
    n = int(input('''Digite qualquer número negativo para encerrar.\nInsira o número desejado: '''))
    for tab in range(1, 11):
        resultado = tab * n
        print(f'{tab} x {n} = {resultado}')
    if n < 0:
        break
    print('-*' * 23)
print('-*' * 23)
print('Obrigado por confiar em nós. Até logo!')