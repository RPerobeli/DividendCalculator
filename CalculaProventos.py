import pandas as pd
import ReadExtracts as RE
import os
import datetime as dt

os.system('cls' if os.name == 'nt' else 'clear')

mesInicio = 1
anoInicio = 2022
mesFim = 1
anoFim = 2023


dataInicio = dt.datetime(anoInicio, mesInicio, 1)
dataFim = dt.datetime(anoFim, mesFim, 1)

df = RE.LerExtratosCSV_Clear()
df['Liquidação'] = pd.to_datetime(df['Liquidação'], format="%d/%m/%Y")

filtroData = (df['Liquidação'] > dataInicio) & (df['Liquidação'] <= dataFim)
df = df.loc[filtroData]

RendimentosTotais = df.query(f'Descrição.str.contains("RENDIMENTO") or Descrição.str.contains("DIVIDENDOS") or  Descrição.str.contains("JUROS S/CAPITAL")')
Valores = RendimentosTotais['Valor'].replace(',', '.',regex=True)
Valores = Valores.astype(float)
print(f'Total de dividendos do período: {Valores.sum()}')