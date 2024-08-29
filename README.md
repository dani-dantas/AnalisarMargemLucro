# Análise de Preços e Margem de Lucro

Este projeto realiza uma análise de preços e margens de lucro de uma loja de peças de moto, utilizando a biblioteca pandas para manipulação de dados e matplotlib para visualização. A análise inclui o cálculo da margem de lucro, lucro total, e visualizações para identificar produtos com baixa margem de lucro.

## Estrutura do Projeto

- dados.csv: Arquivo CSV contendo os dados dos produtos, preços de venda, custos de aquisição e quantidades vendidas.
- analise.py: Script Python que realiza a análise dos dados.

## Dependências

Certifique-se de ter as seguintes bibliotecas Python instaladas:

- pandas
- matplotlib

### O script irá:
1. Carregar e processar os dados do CSV.
2. Calcular a margem de lucro por produto.
3. Calcular o lucro total estimado.
4. Gerar visualizações como histogramas e gráficos de barras.
5. Exibir produtos com margem de lucro abaixo de 10%.

## Saída

1. Margem de Lucro Média, Mínima e Máxima: Exibe um resumo das margens de lucro.
2. Distribuição da Margem de Lucro: Um histograma mostrando a distribuição das margens de lucro entre os produtos.
3. Produtos com Margem de Lucro Baixa: Lista e gráfico de produtos cuja margem de lucro é inferior a 10%.
4. Lucro Total Estimado: Exibe o lucro total estimado para todos os produtos.

## Personalização

O critério para definir "margem de lucro baixa" pode ser alterado no script, ajustando o valor limite de 10% para qualquer outro valor desejado.
