# main.py

import json
from ixc_automacao import IXCAutomacao

def carregar_credenciais(caminho: str) -> dict:
    """
    Carrega as credenciais do arquivo JSON fornecido.

    :parametro caminho: O caminho do arquivo de credenciais.
    :return: Um dicionário contendo as credenciais.
    """
    with open(caminho, 'r') as arquivo:
        return json.load(arquivo)

def main():
    credenciais = carregar_credenciais('config.json')
    usuario = credenciais['usuario']
    senha = credenciais['senha']

    automacao = IXCAutomacao(usuario, senha)
    automacao.login()
    automacao.processar_clientes()

if __name__ == "__main__":
    main()
