import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv')

df['Preço de venda'] = df['Preço de venda'].replace({'R\$ ': ''}, regex=True).astype(float)
df['Custo de aquisição'] = df['Custo de aquisição'].replace({'R\$ ': ''}, regex=True).astype(float)

print(df.head())

df['Margem de Lucro (%)'] = ((df['Preço de venda'] - df['Custo de aquisição']) / df['Preço de venda']) * 100

df['Lucro Total'] = (df['Preço de venda'] - df['Custo de aquisição']) * df['Quantidade vendida']

print(df.head())

margem_media = df['Margem de Lucro (%)'].mean()
margem_minima = df['Margem de Lucro (%)'].min()
margem_maxima = df['Margem de Lucro (%)'].max()

print(f"Margem de Lucro Média: {margem_media:.2f}%")
print(f"Margem de Lucro Mínima: {margem_minima:.2f}%")
print(f"Margem de Lucro Máxima: {margem_maxima:.2f}%")

plt.figure(figsize=(10, 6))
df['Margem de Lucro (%)'].hist(bins=20)
plt.title('Distribuição da Margem de Lucro (%)')
plt.xlabel('Margem de Lucro (%)')
plt.ylabel('Número de Produtos')
plt.grid(False)
plt.show()

produtos_margem_baixa = df[df['Margem de Lucro (%)'] < 10]
print(f"Produtos com margem de lucro abaixo de 10%: {len(produtos_margem_baixa)}")
print(produtos_margem_baixa[['Nome', 'Margem de Lucro (%)', 'Lucro Total']])

produtos_margem_baixa.plot(kind='bar', x='Nome', y='Margem de Lucro (%)', figsize=(12, 6), color='orange')
plt.title('Produtos com Margem de Lucro Abaixo de 10%')
plt.xlabel('Produto')
plt.ylabel('Margem de Lucro (%)')
plt.xticks(rotation=45, ha='right')
plt.grid(False)
plt.show()

lucro_total = df['Lucro Total'].sum()
print(f"Lucro Total Estimado: R$ {lucro_total:.2f}")