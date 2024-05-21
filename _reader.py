import pandas as pd
from _sender import Sender

def limpar_nome_coluna(nome):
    # Função para limpar os nomes das colunas
    return nome.strip().lower().replace(" ", "_")


def Reader():
    path = "planos_funcionarios.xlsx"
    dados = pd.read_excel(path, header=None)

    # Limpa os nomes das colunas
    dados.columns = [limpar_nome_coluna(nome) for nome in dados.iloc[0]]
    dados = dados.drop(0)  # Corrigido para remover a primeira linha (índice 0)
    dados = dados.where(pd.notna(dados), None)  # Substitui NaN por None
    vidas = dados.to_dict(orient="records")

    # Envia vida individualmente para request da api
    for vida in vidas:
        plano_selecionado = vida["plano"]
        vida["planos"] = [plano_selecionado]
        del vida["plano"]
        Sender(vida)

