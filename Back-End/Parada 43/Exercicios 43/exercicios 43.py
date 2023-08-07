## 1) Faça um programa em que o usuário digita dois valores e o resultado da soma é exibido na tela.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

total = num1+num2

print(f'O total da soma entre {num1} e {num2} é de: {total}')


## 2) Faça um programa em que o usuário precisa cadastrar nome, idade, telefone e e-mail. Depois mostre os valores digitados na tela.

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
telefone = input('Digite seu número: ')
email = input('Digite seu email: ')

print('Nome:',nome)
print('Idade: ',idade)
print('Telefone', telefone)
print('Email: ',email)

## 3) Faça um programa no qual o usuário precisa cadastrar as informações de um produto: código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra.
valor_total = 0
for i in range(3):
    nome = input(f'Digite o nome do {i+1}º produto: ')
    codigo = input(f'Digite o código do produto {nome}: ')
    quantidade = int(input(f'Quantidades que deseja levar: '))
    preco = float(input(f'Digite o valor unitário R$'))

    print(f'{i+1}º Produto cadastrado: {nome}, {codigo}, {quantidade}, {preco:.2f}')

    valor_produto = quantidade * preco

    valor_total += valor_produto

print (f'Valor total: R${valor_total:.2f}')

## 4) Faça um programa que converte centímetros em metros.

cm = int(input('Digite o valor em cm: '))
m = cm/100

print(f'O valor de {cm}cm para metros é de: {m}m')


## 5) Faça um programa que calcule a área de um quadrado/retângulo.


#Retângulo 
print('Calculo área do retângulo')
w = int(input('Informe o valor da base do retângulo: '))
h = int(input('Informe o valor da altura do retângulo: '))
total = w * h
print('A área do retângulo é de: ',total)

#Quadrado

print('Calculo área do quadrado')
x = int(input('Digite o valor de um lado do quadrado: '))
a = x**2
print(f'a área do quadrado é: {a}')


