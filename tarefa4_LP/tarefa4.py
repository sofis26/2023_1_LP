# Crie um programa que leia o código de um produto a ser vendido e a quantidade a ser vendida. (
# Para cada venda. Mostre o valor da venda (FALTOU) e armazene na lista 'l_produtos_vendidos' o codigo do produto.
#
# As vendas encerram ao digitar 'fim' no código do produto.
# No final, faça uma consulta na lista 'l_produtos_vendidos' mostrando:
# -Quais os produtos vendidos.
#
# Usar a seguinte lista de produtos: l_produtos = [111, 222, 333, 444, 555, 666, 777]   (FEITO)


# Considerar apenas a venda de um produto por cliente.
# Considerar o código do produto como um número inteiro.
# Considerar que os produtos 111, 222 e 333 custam R$ 10.50   (FEITO)
# Considerar que os produtos 444, 555 e 666 custam R$ 12.00 e (FEITO)
# Considerar que o produto 777 custa R$ 15.30.   (FEITO)

# Validar:
# Se o produto existe.
# Se o código e o valor são válidos.


l_produtos = [111, 222, 333, 444, 555, 666, 777]
val_ido = ["fim", "111", "222", "333", "444", "555", "666", "777" ]
l_produtos_vendidos = []
mercadoria = 0
quantidade = 0


while True:
    preco = [10.50, 12.00, 15.30]
    print("Escolha seu(s) produto(s):", l_produtos)

    mercadoria = input("Digite o código do produto (ou 'fim' para encerrar):")

    if mercadoria in val_ido:
        if mercadoria.lower() == 'fim':
            break

    quantidade = input("Digite a quantidade: ")

    if mercadoria == "111":
        print("Total:", preco[0]* quantidade)
        l_produtos_vendidos.append(111)

    if l_produtos == "222":
        print("Total:", preco[0]* quantidade)
        l_produtos_vendidos.append(222)

    if l_produtos == "333":
        print("Total:", preco[0]* quantidade)
        l_produtos_vendidos.append(333)

    if l_produtos == "444":
        print("Total:", preco[1]* quantidade)
        l_produtos_vendidos.append(444)

    if l_produtos == "555":
        print("Total:", preco[1]* quantidade)
        l_produtos_vendidos.append(555)

    if l_produtos == "666":
        print("Total:", preco[1]* quantidade)
        l_produtos_vendidos.append(666)

    if l_produtos == "777":
        print("Total:", preco[2]* quantidade)
        l_produtos_vendidos.append(777)

else:
    print("Inválido. Responda novamente.")


print("\nProdutos vendidos:", l_produtos_vendidos)