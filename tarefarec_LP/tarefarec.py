#Nome da aluna: Sofia Pedroso Cotta

#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for
# informado um valor igual a -1 (que não deve ser armazenado).   (FEITO)
#Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;   (FEITO)
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;   (FEITO)
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;   (FEITO)
#Calcule e mostre a soma dos valores;    (FEITO)
#Calcule e mostre a média dos valores;   (FEITO)
#Calcule e mostre a quantidade de valores acima da média calculada;  (FEITO)
#Calcule e mostre a quantidade de valores abaixo de sete;    (FEITO)
#Encerre o programa com uma mensagem;    (FEITO)

# ler vários números   (FEITO)
# quando -1 for digitado o programa encerra a entrada de dados  (FEITO)
# Mostre a quantidade de valores que foram lidos;  (FEITO)



notas = []
acima_da_media = []
abaixo_de_7 = []


while True:

    valor = int(input("Digite um número: "))
    if valor == -1:
        break
    notas.append(valor)

print("--------------*-------------")
print("Total de valores sitados:", len(notas))
print("Valores um ao lado do outro:", notas)

soma = 0
aux = -1
for i in range(len(notas)):
    print(notas[aux])
    aux = aux - 1
    soma = soma + notas[i]
print("A soma é:", soma)
media = soma/len(notas)
print("A média é:", media)

for i in range(len(notas)):
    if notas[i] > media:
        acima_da_media.append(notas[i])

    if notas[i] < 7:
        abaixo_de_7.append(notas[i])

print("Valores acima da média:",acima_da_media)
print("Valores abaixo de sete:", abaixo_de_7)

print("Programa encerrado!")


#append:
# colocar um valor dentro de uma lista
# antes do append nome da lista
# dentro do parênteses é o que quero colocar dentro da lista
# break = finaliza o loop


