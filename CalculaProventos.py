import pandas as pd

df = pd.read_csv('extrato-2022.12.01-2022.12.31.csv', sep = ';')

print(df.columns)
RendimentosTotais = df.query(f'Descrição.str.contains("RENDIMENTO") or Descrição.str.contains("DIVIDENDOS") or  Descrição.str.contains("JUROS S/CAPITAL")')
# print(RendimentosTotais)
Valores = RendimentosTotais['Valor'].replace(',', '.',regex=True)
Valores = Valores.astype(float)
print(Valores.sum())