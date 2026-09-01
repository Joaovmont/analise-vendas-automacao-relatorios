# Automação de Ranking de Vendas

## Objetivo do Projeto

Este projeto tem como objetivo automatizar a análise do faturamento de diferentes lojas e a geração de um ranking de vendas.

A aplicação lê os dados de vendas de arquivos Excel referentes a diferentes cidades, calcula o faturamento de cada loja, organiza os resultados em ordem decrescente e gera automaticamente uma mensagem contendo o ranking.

Ao final do processo, o ranking é enviado por e-mail de forma automatizada, reduzindo a necessidade de realizar manualmente os cálculos, a organização dos dados e o envio das informações.

## Tecnologias Utilizadas

* Python
* Pandas
* Excel
* Yagmail

## Funcionamento

O programa utiliza uma lista com as cidades que possuem arquivos de vendas:

```python
lista_cidades = ["BH", "DF", "Manaus", "Rio", "Salvador", "SP"]
```

Para cada cidade, o programa:

1. Localiza e lê o arquivo Excel correspondente.
2. Acessa a coluna de vendas da planilha.
3. Calcula o faturamento total da loja.
4. Armazena o resultado em um dicionário.
5. Converte os resultados para um DataFrame utilizando Pandas.
6. Organiza as lojas em ordem decrescente de faturamento.
7. Formata os valores monetários.
8. Gera automaticamente uma mensagem com o ranking.
9. Utiliza a biblioteca Yagmail para enviar o resultado por e-mail.

## Exemplo do Processo

Os arquivos de entrada seguem o padrão:

```text
Loja BH.xlsx
Loja DF.xlsx
Loja Manaus.xlsx
Loja Rio.xlsx
Loja Salvador.xlsx
Loja SP.xlsx
```

O programa processa os arquivos e produz um ranking semelhante a:

```text
Vendas
SP        R$ XXX.XXX,XX
BH        R$ XXX.XXX,XX
Salvador  R$ XXX.XXX,XX
Rio       R$ XXX.XXX,XX
Manaus    R$ XXX.XXX,XX
DF        R$ XXX.XXX,XX
```

Os valores reais dependem dos dados presentes nas planilhas utilizadas como entrada.

## O que foi aprendido

O desenvolvimento deste projeto permitiu aplicar conhecimentos de Python em uma situação prática de análise e automação de dados.

Os principais aprendizados foram:

* Leitura e manipulação de arquivos Excel utilizando Pandas.
* Utilização de listas, dicionários, estruturas de repetição e variáveis em Python.
* Cálculo e organização de informações a partir de uma base de dados.
* Criação e manipulação de DataFrames.
* Ordenação de dados para criação de um ranking.
* Formatação de valores monetários.
* Geração dinâmica de mensagens utilizando f-strings.
* Automação do envio de informações por e-mail utilizando Yagmail.
* Integração entre diferentes etapas de um processo utilizando Python.

Além dos conhecimentos técnicos, o projeto demonstrou como a programação pode ser utilizada para transformar uma atividade manual e repetitiva em um processo automatizado, reduzindo o trabalho operacional e facilitando a obtenção das informações.

## Possíveis Melhorias

Como evolução do projeto, algumas funcionalidades poderiam ser implementadas:

* Utilização de variáveis de ambiente para armazenar credenciais de e-mail com maior segurança.
* Tratamento de erros para arquivos inexistentes ou planilhas com dados inválidos.
* Criação de gráficos para complementar o ranking.
* Geração automática de arquivos de relatório.
* Integração com bancos de dados SQL.
* Criação de uma interface para facilitar a execução da automação.
* Automatização da atualização das bases de vendas.

## Autor

João Vitor Monteiro Moreira

Estudante de Análise e Desenvolvimento de Sistemas, com interesse em Análise de Dados, Inteligência Artificial, Engenharia de Dados e Automação.

GitHub: https://github.com/Joaovmont
LinkedIn: https://linkedin.com/in/joaovmmoreira/
