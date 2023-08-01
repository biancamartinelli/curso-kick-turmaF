soma_total = 0

for i in range(10):
    numero = int(input(f"Digite o {i + i}º número: "))
    soma_total += numero

print("A soma total dos 10 número é: ", soma_total)


#-----------------------

maior_preco = 0
soma_precos = 0

for i in range(3):
    codigo = input(f"Digite o código do {i + 1}º produto: ")
    preco = float(input(f"Digite o preço do {i + 1}º produto: "))
    
    if preco > maior_preco:
        maior_preco = preco
        
    soma_precos += preco
    
#-----------------------

soma_inferiores_40 = 0

for i in range(10):
    numero =  int(input(f"Digite o {i + 1}º numero: "))
    if numero < 40:
        soma_inferiores_40 = numero
print("A soma dos números inferiores a 40 é:", soma_inferiores_40)