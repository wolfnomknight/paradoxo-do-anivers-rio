# Paradoxo do aniversário, por Wolfnom ~ Sergio A. Knapik
# Um pequeno programa para simular a probabilidade de aniversários
# Codado em 2022

import random


def main():
    number_of_bdays = 0

    print("O Paradoxo do Aniversário, por Wolfnom\n")

    # Continua pedindo um número entre 1 e 100 até receber uma entrada válida
    valid_number = False
    while not valid_number:
        number_of_bdays = input("Quantas datas devo gerar aleatoriamente? Digite um número entre 1 e 100.\n")
        try:
            number_of_bdays = int(number_of_bdays)
        except ValueError:
            print("Entrada inválida! Deve ser um nmúmero!\n")
        else:
            if number_of_bdays > 0 and number_of_bdays < 101:
                valid_number = True
            else:
                print("Número inválido! Deve ser entre 1 e 100!\n")

    # Gera a quantidade solicitada de datas aleatórias, exibe a calcula repetições
    list_of_bdays = birthday_generator(number_of_bdays)
    print(f"\n{format_bday_list(list_of_bdays)}")
    print(f"\nNessa lista há {bday_list_count(list_of_bdays)} aniversários repetidos.")

    print(f"\nGerando {number_of_bdays} datas aleatórias 100.000 vezes\n")
    input("Pressione enter para continuar")
    print(f"0 datas geradas...")

    # Agora faz o mesmo mas 100k vezes: gera datas e verifica repetições
    repetitions = 0
    for generation in range(1, 100001):

        # De cada vez, gera uma lista de datas aleatórias e verifica se há datas repetidas,
        # se sim, conta uma repetição
        if bday_list_count(birthday_generator(number_of_bdays)) > 0:
            repetitions += 1

        # Informa ao usuário qual grupo de datas está sendo processado, porque isso pode demorar um pouquinho
        if generation == 100000:
            print(f"100.000 grupos gerados! São {number_of_bdays*generation} datas aleatórias verificadas!")
        elif generation % 10000 == 0:
            print(f"{generation} grupos gerados ({number_of_bdays*generation} datas)...")

    # Exibe a mensagem final com a porcentagem de chance de datas repetidas
    print(f"Dos 100.000 grupos com {number_of_bdays} datas geradas, houve aniversários repetidos em {repetitions}.\n"
          f"Isso significa uma chance de {repetitions/1000}% de repetições. Interessante, não?")


def birthday_generator(how_many_bdays):
    # Poderia ter simplificado esta parte usando o módulo datetime, mas eu queria usar só o random dessa vez
    # Lista de meses para seleção aleatória
    list_of_months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro",
                      "outubro", "novembro", "dezembro"]
    # Listas de referência para selecionar o dia aleatoriamente
    list_of_31_days_months = ["janeiro", "março", "maio", "julho", "agosto", "outubro", "dezembro"]
    list_of_30_days_months = ["abril", "junho","setembro", "novembro"]

    list_of_bdays = list()

    # Gerando as datas aleatórias em quantidade igual à solicitada pelo usuário
    for i in range(0, how_many_bdays):
        # Primeiro, pega um mês aleatório
        month = random.choice(list_of_months)
        # Depois, escolhe um dia aleatório dentro das possibilidades de cada mês
        if month in list_of_31_days_months:
            day = random.randint(1, 32)
        elif month in list_of_30_days_months:
            day = random.randint(1, 31)
        else:
            day = random.randint(1, 29)
        # Então junta os dois valores aleatórios numa string
        list_of_bdays.append(f"{day} de {month}")

    return list_of_bdays


def format_bday_list(list_of_bdays):
    # Aqui é formatada a lista para ficar mais bonitinha quando exibida na tela
    bday_text = str()
    # A string resultando começa com este texto, contendo quantas datas foram geradas
    bday_text_result = f"Aqui temos {len(list_of_bdays)} datas de aniversário:\n"

    # Juntando as datas numa string
    for bday in list_of_bdays:
        bday_text += f"{bday}, "
    # Retirando a última vírgula da string
    bday_text = bday_text[:-2]
    # Juntando o início do texto com a lista em forma de string
    bday_text_result += bday_text

    return bday_text_result


def bday_list_count(list_of_bdays):
    # Começamos com nenhum aniversário repetido
    repeated_bdays = 0
    # Então verificamos para cada data...
    for bday in list_of_bdays:
        n = list_of_bdays.count(bday)
        # ...se ela aparece mais do que uma vez na lista. Se sim, tem repetição!
        if n > 1:
            repeated_bdays += 1
    # Retorna a quantidade de repetições
    return repeated_bdays


main()
