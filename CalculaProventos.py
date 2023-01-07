import pandas as pd
import ReadExtracts as RE
import os

os.system('cls' if os.name == 'nt' else 'clear')

df = RE.LerExtratosCSV_Clear()
RendimentosTotais = df.query(f'Descrição.str.contains("RENDIMENTO") or Descrição.str.contains("DIVIDENDOS") or  Descrição.str.contains("JUROS S/CAPITAL")')
Valores = RendimentosTotais['Valor'].replace(',', '.',regex=True)
Valores = Valores.astype(float)
print(f'Total de dividendos do período: {Valores.sum()}')