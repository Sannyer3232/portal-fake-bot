from __future__ import annotations

import csv
from pathlib import Path

CSV_PATH = Path(__file__).with_name("dados.csv")

def buscar_dados_por_cpf(cpf: str) -> str | None:
    cpf_normalizado = ''.join(filter(str.isdigit, str(cpf)))

    if not cpf_normalizado:
        return None

    with CSV_PATH.open(newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_cpf = ''.join(filter(str.isdigit, row.get('CPF', '')))
            if row_cpf == cpf_normalizado:
                return '\n'.join(f"{key}: {value}" for key, value in row.items())

    return None