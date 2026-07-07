import pandas as pd

def exportar_dados(nome_arquivo: str):
    print("Iniciando exportação de dados...")
    dados_excel = pd.read_excel('nome_arquivo', sheet_name='Planilha1')

    print("Exportando dados...")
    dados_excel.to_csv('arquivo_convertido.csv', index=False, sep=';', encoding='utf-8-sig')

    print("Dados exportados com sucesso!")