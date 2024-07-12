#Faça um algoritmo em que leia infinitos números inteiros. O algoritmo finaliza ao ser digitado o número 0(zero) ou a palavra fim.
#Se o número digitado for negativo, armazene em uma lista chamada lst_negativos.
#Quando finalizar o algoritmo, mostre o menor e o maior número negativo de lst_negativos, ou a mensagem: "Não foi digitado nenhum número negativo".
#Se o número digitado estiver no intervalo entre 20 e 60, leia outro número e imprima todos inteiros entre os dois em ordem crescente, ou a mensagem: "Não há números inteiros entre o primeiro e o segundo.".
#Se o número digitado estiver no intervalo entre 40 e 80 e for par, leia outro número e imprima todos o inteiros PARES entre os dois números digitados em ordem decrescente, ou a mensagem:
#"Não há números inteiros neste intervalo".
#Para os números que não estiverem nos critérios a cima mostrar a mensagem: "Número Ok.".

lst_negativos = []
min_negativo = None
max_negativo = None

while True:
    entrada = input("Digite um número inteiro (0 ou 'fim' para sair): ")

    if entrada == '0' or entrada.lower() == 'fim':
        break

    numero = int(entrada)

    if numero < 0:
        lst_negativos.append(numero)

        if min_negativo is None or numero < min_negativo:
            min_negativo = numero

        if max_negativo is None or numero > max_negativo:
            max_negativo = numero

    elif 20 <= numero <= 60:
        segundo_numero = int(input("Digite outro número inteiro: "))

        if numero < segundo_numero:
            for i in range(numero, segundo_numero + 1):
                print(i, end=" ")
            print()
        else:
            print("Não há números inteiros entre o primeiro e o segundo.")

    elif 40 <= numero <= 80 and numero % 2 == 0:
        segundo_numero = int(input("Digite outro número inteiro: "))

        if segundo_numero % 2 != 0:
            segundo_numero -= 1

        if numero > segundo_numero:
            for i in range(numero, segundo_numero -1, -2):
                print(i, end=" ")
            print()
        else:
            print("Não há números inteiros neste intervalo.")

    else:
        print("Número ok.")

if lst_negativos:
    print("Menor número negativo:", min_negativo)
    print("Maior número negativo:", max_negativo)
else:
    print("Não foi digitado nenhum número negativo.")
