import os
from pathlib import Path
from cadastro import ler_planilha, processar_cadastros
from consulta import buscar_dados_por_cpf
from exportacao import exportar_dados


def orquestrador():
    print("=" * 50)
    print("INICIANDO ORQUESTRADOR DO BOT")
    print("=" * 50)

    # 1. Preparação/Exportação dos dados

    planilha_origem = "Dados_do_roteiro_06.xlsx"

    if os.path.exists(planilha_origem):
        print("\n[Passo 1] Convertendo base de dados Excel para CSV...")
        # Chamando a função de exportação
        exportar_dados(planilha_origem)

        # Ajuste de contingência: consulta.py procura por 'dados.csv' no mesmo diretório
        # Se o exportacao.py gerou 'arquivo_convertido.csv', vamos renomear/copiar para 'dados.csv'
        if os.path.exists("arquivo_convertido.csv"):
            if os.path.exists("dados.csv"):
                os.remove("dados.csv")
            os.rename("arquivo_convertido.csv", "dados.csv")
    else:
        print(
            f"\n[Aviso] Planilha {planilha_origem} não encontrada. Pulando exportação."
        )

    # 2. Processamento de Cadastros
    print("\n[Passo 2] Iniciando o processamento e cadastro de usuários...")
    df_usuarios = ler_planilha(planilha_origem, "Usuarios")

    if df_usuarios is not None:
        # Executa a simulação de cadastro na tela
        processar_cadastros(df_usuarios)

        # 3. Simulação de Consulta automatizada
        print("\n[Passo 3] Iniciando consultas de verificação (Exemplo)...")
        for _, linha in df_usuarios.head(2).iterrows():
            cpf_teste = str(linha["CPF"])
            print(f"\nBuscando dados no CSV para o CPF: {cpf_teste}")

            resultado = buscar_dados_por_cpf(cpf_teste)
            if resultado:
                print("--- Registro Encontrado ---")
                print(resultado)
                print("---------------------------")
            else:
                print(
                    f"Aviso: CPF {cpf_teste} não foi encontrado no arquivo 'dados.csv'."
                )
    else:
        print("Erro: Não foi possível carregar os dados para o cadastro.")

    print("\n=" * 50)
    print("ORQUESTRAÇÃO FINALIZADA COM SUCESSO!")
    print("=" * 50)


if __name__ == "__main__":
    orquestrador()