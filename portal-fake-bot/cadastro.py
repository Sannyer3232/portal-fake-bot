import pandas as pd


def ler_planilha(caminho_arquivo, nome_aba=0):
    """
    Lê uma planilha Excel e retorna um DataFrame.

    Parâmetros:
        caminho_arquivo (str): Caminho do arquivo Excel.
        nome_aba (str ou int): Nome ou índice da aba.

    Retorno:
        pandas.DataFrame
    """
    try:
        df = pd.read_excel(caminho_arquivo, sheet_name=nome_aba)
        return df

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return None

    except Exception as erro:
        print(f"Erro ao ler a planilha: {erro}")
        return None


def processar_cadastros(df):
    for _, linha in df.iterrows():
        print("##CADASTRANDO REGISTRO")
        print(f"Nome: {linha['Nome']} {linha['Sobrenome']}")
        print(f"CPF: {linha['CPF']}")
        print(f"E-mail: {linha['E-mail']}")
        print('##CADASTRO REALIZADO!')
        print("-" * 40)



if __name__ == '__main__':
    df = ler_planilha('Dados_do_roteiro_06.xlsx', 'Usuarios')
    if df is not None:
        processar_cadastros(df)
