import pandas as pd
import matplotlib.pyplot as plt

def classificar(prep):
    if prep > 5:
        return 'Chuvoso'
    elif prep == 0:
        return 'Seco'
    else:
        return 'Neutro'

df = pd.read_csv('dados_meteorologicos.csv')

print("Colunas disponíveis no DataFrame:", df.columns)

if 'Data' not in df.columns:
    raise KeyError("A coluna 'Data' não foi encontrada no DataFrame. Verifique o arquivo CSV.")

df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)

df['mes'] = df['Data'].dt.month

status = df.groupby('mes')['Temp. Inst (C)'].agg(['mean', 'max', 'min']).round(2)
print("Estatísticas de temperatura por mês")
print(status)

precipitacao_mensal = df.groupby('mes')['Precipitacao (mm)'].sum()

plt.figure(figsize=(10, 6))
precipitacao_mensal.plot(kind='bar')
plt.title('Precipitação Total Mensal')
plt.xlabel('Mês')
plt.ylabel('Precipitação (mm)')
plt.xticks(ticks=range(12), labels=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.tight_layout()

mais_quentes = df.nlargest(10, 'Temp. Inst (C)')[['Data', 'Temp. Inst (C)']]
mais_frios = df.nsmallest(10, 'Temp. Inst (C)')[['Data', 'Temp. Inst (C)']]

print("\n10 Dias Mais Quentes:")
print(mais_quentes)
print("\n10 Dias Mais Frios:")
print(mais_frios)

df['classificacao'] = df['Precipitacao (mm)'].apply(classificar)
print("\nContagem de dias por classificação:")
print(df['classificacao'].value_counts())
plt.show()
