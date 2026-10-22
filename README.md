# Análise Exploratória dos Preços de Aluguel em São Paulo

**Desafio SYNAPTA 2026 — Etapa 2**

**Instituição:** UNINASSAU — Maceió/AL  
**Curso:** Ciência da Computação  
**Modalidade:** Análise exploratória de dados  
**Opção escolhida:** 1 — Preços de aluguel em São Paulo

## 1. Objetivo

Investigar como características dos imóveis, especialmente localização, área e quantidade de quartos, estão associadas aos valores de aluguel anunciados na cidade de São Paulo.

**Pergunta orientadora:** quais características parecem acompanhar os maiores e os menores preços de aluguel e o que os dados não permitem concluir?

## 2. Fonte dos dados

Dataset: Sao Paulo Housing Prices.

Fonte: [Kaggle — Sao Paulo Housing Prices](https://www.kaggle.com/datasets/renatosn/sao-paulo-housing-prices)

A base analisada contém 11.657 anúncios e oito variáveis.

A licença e as condições de redistribuição deverão ser verificadas antes da publicação do repositório.

## 3. Tecnologias utilizadas

- Python 3.12
- Pandas
- Matplotlib
- Visual Studio Code
- Git e GitHub — previstos para o versionamento e publicação

## 4. Metodologia

A análise foi organizada nas seguintes etapas:

1. Carregamento e inspeção dos dados.
2. Identificação de valores ausentes e duplicações.
3. Investigação de inconsistências e valores extremos.
4. Análise da distribuição dos aluguéis.
5. Comparação dos preços médios entre localidades.
6. Investigação da relação entre área, quartos e aluguel.
7. Construção de gráficos e interpretação dos resultados.

## 5. Resultados preliminares

A análise identificou:

- Aluguel médio de R$ 3.250,81 e mediano de R$ 2.415,00.
- Diferenças expressivas nos preços médios entre as localidades analisadas.
- Correlação positiva de 0,667 entre área e aluguel.
- Tendência geral de aluguéis mais elevados em imóveis com maior quantidade de quartos.
- Influência diferente de uma observação extrema conforme o grupo analisado.

As conclusões detalhadas estão no arquivo `CONCLUSOES.md`.

## 6. Limitações

Os resultados representam os anúncios presentes no dataset, não necessariamente contratos efetivados ou todo o mercado imobiliário de São Paulo.

As associações identificadas não demonstram causalidade.

As localidades apresentam quantidades diferentes de anúncios, e o limite mínimo de 30 registros é uma decisão exploratória deste estudo.

## 7. Estado do projeto

Projeto em desenvolvimento para a segunda etapa do processo seletivo SYNAPTA 2026.

Ainda serão acrescentados os gráficos, as instruções de reprodução, as dependências e a declaração transparente de uso de inteligência artificial generativa.

## 8. Como executar o projeto

### Pré-requisitos

- Python 3.12
- Git (opcional para baixar o repositório)
- Acesso ao dataset original

### Preparação do ambiente

1. Baixe o repositório do projeto.
2. Abra a pasta do projeto no terminal.
3. Instale as dependências com:

```bash
python -m pip install -r requirements.txt
```

4. Baixe o dataset *Sao Paulo Housing Prices* na página do [Kaggle](https://www.kaggle.com/datasets/renatosn/sao-paulo-housing-prices).
5. Extraia o arquivo CSV e coloque-o na raiz do projeto com o nome `data.csv`.

### Executando a análise

No terminal, execute:

```bash
python analise.py
```

O programa apresentará os resultados estatísticos e as verificações realizadas.

Os gráficos produzidos serão salvos automaticamente na pasta `graficos/`.

### Ambiente utilizado no desenvolvimento

- Python 3.12
- Pandas 3.1.0
- Matplotlib 3.11.2
- Visual Studio Code
- Windows

As instruções ainda serão validadas em um ambiente Python isolado antes da entrega final.
