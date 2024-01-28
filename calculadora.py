def menu():
    print('''
[1] Somar 
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Novos numeros
[6] Sair do programa''')

lista = []
for i in range(1,3):
    n = float(input('Numero {}:'.format(i)))
    lista.append(n)
menu()
esc = int(input('Qual a sua escolha:')) 
while esc != 6:
    if (esc == 1):
        r = sum(lista)
        print('{} + {} = {}'.format(lista[0],lista[1],r))
    elif (esc == 2):
        r = lista[0] - lista[1]
        print('{} - {} = {}'.format(lista[0],lista[1],r))
    elif (esc == 3):
        r = lista[0] * lista[1]
        print('{} X {} = {}'.format(lista[0],lista[1],r))
    elif (esc == 4):
        r = lista[0] / lista[1]
        print('{} : {} = {}'.format(lista[0],lista[1],r))
    elif (esc == 5):
        lista.clear()
        lista = []
        for i in range(1,3):
            n = float(input('Numero {}:'.format(i)))
            lista.append(n)
    else:
        print('OPÇÂO INVALIDA')
    menu() 
    esc = int(input('Deseja continuar:')) 
