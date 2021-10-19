# github.com/angeloo999
def numero():
    global x, y
    x = int(input('Primeiro número: '))
    y = int(input('Segundo número: '))

def somar():
    print('O resultado é: ', x+y)
    input()

def subtrair():
    print('O resultado é: ', x-y)
    input()

def multiplicar():
    print('O resultado é: ', x*y)
    input()

def divisao():
    if y == 0:
        print('Não se pode dividir por 0!')
    else:
        print('O resultado é: ', x/y)
        input()

def erro():
    print('Erro!')

menu = '''
1. Somar
2. Subtrair
3. Multiplicação
4. Divisão
'''

sw = True
while sw:
    print(menu)
    opcao = int(input('Opção: '))
    if opcao == 1:
        numero()
        somar()
    elif opcao == 2:
        numero()
        subtrair()
    elif opcao == 3:
        numero()
        multiplicar()
    elif opcao == 4:
        numero()
        divisao()
    else:
        erro()
