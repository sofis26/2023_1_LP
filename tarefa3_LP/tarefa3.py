# Crie um programa que leia o nome e a nota para até 40 alunos. (FEITO)
# Armazene o nome e a nota em 2 listas l_nomes, e l_notas (FEITO)
# A nota do aluno deverá ser apena uma das seguintes: A, B, C, D. Aceitar apenas uma destas. (FEITO)
# No final, mostre a quantidade de cada uma das notas dadas e o percentual de aprovados e reprovados. ("Feito" / REPROVAR SÓ OS QUE TIVEREM COM NOTA: D)
# mostre também o nome dos alunos que se destacaram com A (FEITO)
# .
# Critérios para desenvolver a tarefa:
#     - aceitar apenas A,B,C, ou D nas respostas
#     - utilizar listas para armazenar as respostas os nomes e as repostas.
#.    - utilizar funções


def ler_notas_alunos():
    l_nomes = []
    l_notas = []

    for _ in range(40):
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break

        nota = ''
        while nota not in ['A', 'B', 'C', 'D']:
            nota = input("Digite a nota do aluno (A, B, C ou D): ").upper()

        l_nomes.append(nome)
        l_notas.append(nota)

    return l_nomes, l_notas


def contar_notas(l_notas):
    contador = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    for nota in l_notas:
        contador[nota] += 1

    return contador


def calcular_percentual(contador, total):
    percentuais = {}

    for nota, quantidade in contador.items():
        percentuais[nota] = (quantidade / total) * 100

    return percentuais


def mostrar_resultados(l_nomes, l_notas, contador, percentuais):
    print("---- Resultados ----")
    print("Quantidade de notas:")
    for nota, quantidade in contador.items():
        print(f"Nota {nota}: {quantidade}")

    print("\nPercentual de aprovados e reprovados:")
    aprovados = contador['A'] + contador['B'] + contador['C']
    reprovados = contador['D']
    percent_aprovados = (aprovados / sum(contador.values())) * 100
    percent_reprovados = (reprovados / sum(contador.values())) * 100
    print(f"Aprovados: {aprovados} ({percent_aprovados:.2f}%)")
    print(f"Reprovados: {reprovados} ({percent_reprovados:.2f}%)")

    print("\nAlunos que se destacaram com nota A:")
    for nome, nota in zip(l_nomes, l_notas):
        if nota == 'A':
            print(nome)


def main():
    l_nomes, l_notas = ler_notas_alunos()
    total_alunos = len(l_nomes)
    contador = contar_notas(l_notas)
    percentuais = calcular_percentual(contador, total_alunos)
    mostrar_resultados(l_nomes, l_notas, contador, percentuais)


if __name__ == '__main__':
    main()

