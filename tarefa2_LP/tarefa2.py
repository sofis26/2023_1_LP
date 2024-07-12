# Crie um programa que faça 5 perguntas para no mínimo 3 alunos,
# sobre a disciplina de Lógica. As perguntas são:
# "Você estuda pelo menos 2 vezes por semana? s/n: "
# "Você conhece as funções básicas da linguagem? s/n: "
# "Você conhece bem os comandos for, while e if? s/n: "
# "Você consegue fazer os exercícios no tempo adeguado? s/n: "
# "Seu grau de confiança para a disciplina é superior a 50%? s/n: "

# No final seu programa deve emitir uma classificação
#       sobre o desempenho de cada aluno. Se a pessoa responder positivamente:
#       -a 2 questões ela deve ser classificada como "É necessário maior dedicação!",
#       -entre 3 e 4 como "Dá para melhorar mais!" e
#       -5 como "Muito Bem. Agora só falta demonstrar que foste Além do Esperado.".
#       -Caso contrário, ele será classificado como "Ok Não desista. Você consegue.".

# No final, seu programa também deverá mostrar quantas pessoas
# se classificaram com "Muito Bem."

# Critérios para desenvolver a tarefa:
#     - aceitar apenas s/n nas respostas
#     - utilizar listas para armazenar as respostas.



def fazer_perguntas():
    perguntas = [
        "Você estuda pelo menos 2 vezes por semana? s/n: ",
        "Você conhece as funções básicas da linguagem? s/n: ",
        "Você conhece bem os comandos for, while e if? s/n: ",
        "Você consegue fazer os exercícios no tempo adequado? s/n: ",
        "Seu grau de confiança para a disciplina é superior a 50%? s/n: "
    ]

    respostas = []

    for pergunta in perguntas:
        resposta = input(pergunta)
        while resposta.lower() != 's' and resposta.lower() != 'n':
            print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
            resposta = input(pergunta)

        respostas.append(resposta.lower())

    return respostas


def classificar_aluno(respostas):
    total_positivas = respostas.count('s')

    if total_positivas == 2:
        return "É necessário maior dedicação!"
    elif 3 <= total_positivas <= 4:
        return "Dá para melhorar mais!"
    elif total_positivas == 5:
        return "Muito bem. Agora só falta demonstrar que foste além do esperado."
    else:
        return "Ok. Não desista. Você consegue!"


num_alunos = 0
num_muito_bem = 0

while num_alunos < 3:
    print(f"\nAluno {num_alunos + 1}:")
    respostas_aluno = fazer_perguntas()
    classificacao = classificar_aluno(respostas_aluno)

    print(f"\nClassificação: {classificacao}")

    if classificacao == "Muito bem. Agora só falta demonstrar que foste Além do Esperado.":
        num_muito_bem += 1

    num_alunos += 1

print("\nResumo:")
print(f"Total de alunos: {num_alunos}")
print(f"Alunos com classificação 'Muito bem': {num_muito_bem}")
