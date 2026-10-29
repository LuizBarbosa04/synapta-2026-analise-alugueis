# Análise Exploratória dos Preços de Aluguel em São Paulo

**Desafio SYNAPTA 2026 — Etapa 2**

**Instituição:** UNINASSAU — Maceió/AL  
**Curso:** Ciência da Computação  
**Modalidade:** Análise exploratória de dados  
**Opção escolhida:** 1 — Preços de aluguel em São Paulo

## 1. Objetivo

Investigar como localização, área e quantidade de quartos se relacionam com os aluguéis anunciados nos imóveis presentes no dataset de São Paulo.

**Pergunta orientadora:** quais características parecem acompanhar os maiores e os menores preços de aluguel e o que os dados não permitem concluir?

## 2. Fonte dos dados

- **Dataset:** Sao Paulo Housing Prices
- **Fonte:** [Kaggle — Sao Paulo Housing Prices](https://www.kaggle.com/datasets/renatosn/sao-paulo-housing-prices)
- **Licença indicada no Kaggle:** CC0 — Public Domain
- **Tamanho da base analisada:** 11.657 registros e 8 colunas

O dataset original **não está incluído neste repositório**, por decisão de organização do projeto. Para reproduzir a análise, faça o download na fonte indicada e coloque o CSV na raiz do repositório com o nome `data.csv`.

### Variáveis utilizadas

| Coluna | Descrição |
|---|---|
| `address` | Endereço informado no anúncio |
| `district` | Localidade informada no anúncio |
| `area` | Área do imóvel (m²) |
| `bedrooms` | Quantidade de quartos |
| `garage` | Quantidade de vagas de garagem |
| `type` | Tipo de imóvel |
| `rent` | Aluguel anunciado (R$) |
| `total` | Custo total indicado no anúncio (R$) |

As descrições refletem a interpretação utilizada nesta análise; a base não foi tratada como um cadastro de contratos efetivamente negociados.

## 3. Tecnologias utilizadas

- Python 3.12
- Pandas 3.1.0
- Matplotlib 3.11.2
- Visual Studio Code
- Git e GitHub

## 4. Metodologia

A análise exploratória foi desenvolvida nas seguintes etapas:

1. Leitura e inspeção do dataset, composto por 11.657 anúncios e oito variáveis.
2. Verificação de valores ausentes, duplicações exatas e possíveis inconsistências.
3. Identificação de dois registros com área igual a zero, desconsiderados exclusivamente das análises que exigem área positiva.
4. Investigação de valores extremos, incluindo um anúncio de R$ 25.000 para um studio de 24 m², sem exclusão automática.
5. Cálculo de estatísticas descritivas e análise da distribuição dos aluguéis.
6. Comparação entre localidades com pelo menos 30 anúncios e análise de sensibilidade utilizando limites de 20, 30 e 50 registros.
7. Investigação da associação entre área e aluguel, por meio da correlação de Pearson, e comparação dos aluguéis por quantidade de quartos.
8. Cálculo do aluguel por metro quadrado para os 11.655 imóveis com área positiva, investigação de registros com áreas extremamente pequenas e análise de sensibilidade dos limites mínimos de área.
9. Comparação entre quatro tipos de imóveis, considerando quantidade de anúncios, média e mediana, com investigação adicional dos maiores valores de casas em condomínio.
10. Construção e interpretação de seis gráficos, acompanhados de conclusões e limitações metodológicas.

**Decisões metodológicas:** preservar os registros originais sempre que não houver evidência suficiente para comprovar erros; utilizar análises de sensibilidade para examinar a influência dos critérios de seleção; e evitar interpretações causais a partir de associações descritivas.

O limite mínimo de 30 anúncios por localidade é um critério exploratório, não uma garantia de estabilidade ou representatividade estatística.

## 5. Resultados e visualizações

### 5.1 Distribuição dos aluguéis

- **Média:** R$ 3.250,81
- **Mediana:** R$ 2.415,00

A média superior à mediana, junto ao histograma, indica assimetria à direita na distribuição dos aluguéis anunciados.

![Distribuição dos aluguéis](graficos/distribuicao_alugueis.png)

### 5.2 Comparação entre localidades

Entre as localidades com pelo menos 30 anúncios, **Jardim Leonor** apresentou o maior aluguel médio (R$ 7.455,74; 38 anúncios), enquanto **Taboão** apresentou o menor (R$ 1.473,14; 49 anúncios).

![Maiores e menores aluguéis médios por localidade](graficos/aluguel_medio_localidades.png)

Os resultados dependem do critério de inclusão. Na análise de sensibilidade:

| Limite mínimo | Localidades analisadas | Cobertura dos anúncios | Localidade com maior média |
|---|---:|---:|---|
| 20 anúncios | 131 | 61,10% | Alphaville |
| 30 anúncios | 78 | 50,36% | Jardim Leonor |
| 50 anúncios | 38 | 37,47% | Cerqueira César |

### 5.3 Relação entre área e aluguel

Considerando somente os **11.655 imóveis com área positiva**, a correlação de Pearson entre área e aluguel foi **0,667**, indicando associação linear positiva na amostra, sem implicar causalidade.

![Relação entre área e aluguel](graficos/area_vs_aluguel.png)

### 5.4 Quantidade de quartos e aluguel

Há uma tendência geral de aluguéis médios mais altos em imóveis com mais quartos, mas a relação não é perfeitamente crescente e o número de anúncios difere bastante entre grupos.

![Aluguel médio por quantidade de quartos](graficos/aluguel_por_quartos.png)

### 5.5 Investigação de valor atípico

Foi identificado um studio no Planalto Paulista, com **24 m²** e aluguel anunciado de **R$ 25.000**. A exclusão **experimental** desse anúncio reduziu a média geral em aproximadamente **0,057%** e a média dos studios em aproximadamente **0,78%**. O registro foi mantido na análise principal porque não havia evidência suficiente para comprovar erro.

### 5.6 Aluguel por metro quadrado e sensibilidade à área

A análise dos **11.655 imóveis com área positiva** apresentou aluguel médio de **R$ 46,69/m²** e mediano de **R$ 37,50/m²**.

Foram identificados quatro registros com áreas inferiores a 5 m², incluindo uma casa em condomínio com quatro quartos, três vagas de garagem e área declarada de apenas 1 m², representando uma possível inconsistência cadastral.

A exclusão experimental desses quatro registros reduziu a média para **R$ 45,65/m²**, enquanto a mediana permaneceu em R$ 37,50/m².

Na análise de sensibilidade, ao considerar apenas imóveis com área de pelo menos 20 m², a média passou para **R$ 44,94/m²** e a mediana para **R$ 37,29/m²**.

A comparação entre os rankings demonstrou que os imóveis com maiores aluguéis totais não são necessariamente aqueles com os maiores valores por metro quadrado.

**Decisão metodológica:** os registros com áreas positivas foram preservados na análise principal. Os limites mínimos de área foram utilizados exclusivamente para avaliar a sensibilidade dos indicadores, sem excluir definitivamente observações suspeitas.

**Conclusão:** a mediana apresentou maior estabilidade diante dos valores extremos investigados, reforçando a importância da avaliação de qualidade dos dados.

![Sensibilidade do aluguel por metro quadrado](graficos/sensibilidade_aluguel_m2.png)

### 5.7 Comparação dos aluguéis por tipo de imóvel

O dataset apresenta quatro categorias de imóveis: apartamentos (7.194 anúncios), casas (2.841), studios e kitnets (1.381) e casas em condomínio (241).

A comparação mostrou que as **casas em condomínio apresentam o maior aluguel médio (R$ 3.912,55)**, mas sua mediana é de apenas R$ 2.200,00. As casas, por sua vez, apresentam a maior mediana entre as categorias, de R$ 2.600,00.

Os studios e kitnets apresentaram os menores valores de média (R$ 2.127,83) e mediana (R$ 1.850,00).

A investigação das casas em condomínio identificou nove anúncios com aluguel de R$ 15.000,00. A exclusão experimental de cinco desses registros reduziu a média da categoria em aproximadamente **6%**, enquanto a mediana permaneceu inalterada.

Esses resultados demonstram a importância de analisar média e mediana conjuntamente, especialmente quando existem anúncios com valores elevados.

**Limitação:** as categorias diferem em quantidade de anúncios, área e outras características. As diferenças observadas não devem ser interpretadas como efeitos causais do tipo de imóvel.

![Aluguel médio e mediano por tipo de imóvel](graficos/aluguel_por_tipo_imovel.png)

## 6. Principais conclusões

1. **Distribuição dos aluguéis:** a média de R$ 3.250,81 supera a mediana de R$ 2.415,00, indicando assimetria à direita na distribuição dos valores anunciados.
2. **Diferenças entre localidades:** considerando pelo menos 30 anúncios por localidade, Jardim Leonor apresentou o maior aluguel médio (R$ 7.455,74) e Taboão o menor (R$ 1.473,14). Os rankings variam conforme o limite mínimo de anúncios.
3. **Relação entre área e aluguel:** a correlação de Pearson foi de 0,667 nos 11.655 imóveis com área positiva, indicando associação linear positiva, sem comprovar causalidade.
4. **Quantidade de quartos:** observou-se tendência geral de aluguéis mais elevados em imóveis com mais quartos, embora existam exceções e grupos com poucos registros.
5. **Influência de valores extremos:** a retirada experimental do anúncio de R$ 25.000 reduziu a média geral em aproximadamente 0,057% e a média dos studios em aproximadamente 0,78%.
6. **Aluguel por metro quadrado:** foram identificados quatro anúncios com áreas inferiores a 5 m². Sua exclusão experimental reduziu a média do aluguel por m² de R$ 46,69 para R$ 45,65, enquanto a mediana permaneceu em R$ 37,50.
7. **Diferenças por tipo de imóvel:** casas em condomínio apresentaram o maior aluguel médio (R$ 3.912,55), mas não a maior mediana. Isso evidencia a importância de comparar diferentes medidas estatísticas.

As análises detalhadas, as decisões metodológicas, as limitações e a resposta à pergunta orientadora estão documentadas em [CONCLUSOES.md](CONCLUSOES.md).

## 7. Limitações

- Os valores são de **anúncios**, não necessariamente de contratos efetivamente fechados.
- O dataset não representa obrigatoriamente todo o mercado imobiliário de São Paulo.
- As associações observadas **não comprovam causalidade**.
- As localidades têm quantidades diferentes de registros, e a classificação muda com o limite mínimo adotado.
- Características como conservação e localização não foram controladas simultaneamente nas comparações.
- A veracidade do anúncio de R$ 25.000 não foi confirmada externamente.
- As áreas extremamente pequenas não foram verificadas nos anúncios originais.
- O arquivo CSV foi obtido anteriormente; o download diretamente do Kaggle não foi novamente testado durante a auditoria de reprodução.

## 8. Como executar o projeto

### Pré-requisitos

Python 3.12 e acesso ao dataset no Kaggle. Git é opcional se o repositório for baixado como arquivo ZIP.

### Preparação

1. Clone ou baixe este repositório.
2. Abra a pasta do projeto no terminal.
3. Instale as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Baixe o dataset [Sao Paulo Housing Prices](https://www.kaggle.com/datasets/renatosn/sao-paulo-housing-prices) no Kaggle.
5. Extraia o arquivo CSV e coloque-o na **raiz do projeto**, com o nome exato `data.csv`.
6. Execute:

   ```bash
   python analise.py
   ```

O programa apresenta os resultados estatísticos no terminal e gera seis gráficos na pasta `graficos/`. Dependendo do ambiente, pode ser necessário fechar janelas abertas pelo Matplotlib para a execução prosseguir.

### Executando o dashboard interativo

Além da análise exploratória realizada pelo arquivo `analise.py`, o projeto disponibiliza uma interface interativa desenvolvida com **Streamlit**, permitindo explorar os resultados diretamente pelo navegador.

Após instalar as dependências do `requirements.txt` e colocar o arquivo `data.csv` na pasta principal do projeto, execute:

```powershell
python -m streamlit run dashboard.py
```

O Streamlit iniciará um servidor local, normalmente disponível em `http://localhost:8501`.

O dashboard está organizado em quatro abas:

1. **Visão geral:** apresenta indicadores de quantidade de anúncios, média e mediana dos aluguéis e comparação entre tipos de imóveis.
2. **Localidades:** permite visualizar rankings de aluguéis médios, utilizando limites mínimos de 20, 30 ou 50 anúncios.
3. **Aluguel por m²:** apresenta indicadores e análise de sensibilidade conforme diferentes limites mínimos de área.
4. **Qualidade dos dados:** apresenta verificações de valores ausentes, duplicações e registros com áreas potencialmente inconsistentes.

O filtro de tipo de imóvel, disponível na barra lateral, atualiza as análises das três primeiras abas. A aba de qualidade dos dados utiliza a base completa.

**Observação:** o dashboard é uma ferramenta complementar de exploração. Os resultados científicos documentados em `CONCLUSOES.md` foram produzidos a partir da análise original, sem filtros interativos adicionais.

O dataset não está incluído no repositório. Portanto, é necessário baixá-lo da fonte indicada antes de iniciar a interface.

### Verificação de reprodutibilidade realizada

A reprodutibilidade foi avaliada inicialmente por meio da clonagem do repositório público do GitHub para uma pasta independente, com criação de um novo ambiente virtual Python e instalação das dependências declaradas no `requirements.txt`.

Foi utilizada uma cópia local do dataset obtido anteriormente. A execução reproduziu os resultados estatísticos e os quatro gráficos existentes naquela versão do projeto, sem apresentar exceções.

Posteriormente, o projeto foi ampliado com análises do aluguel por metro quadrado, sensibilidade à área mínima e comparação por tipo de imóvel.

Após essas atualizações, foi realizada uma nova execução integral do `analise.py` no ambiente de desenvolvimento, finalizada com **código de saída 0**, sem erros de execução. Também foi confirmada a presença dos seis arquivos de gráficos gerados.

**Limitações da validação:** a versão ampliada ainda não foi reproduzida novamente em um ambiente virtual independente. Além disso, não foi realizado um novo download diretamente da página do Kaggle durante os testes de reprodutibilidade.

## 9. Declaração de uso de inteligência artificial generativa

Foi utilizado **ChatGPT (OpenAI)** como apoio educacional e técnico para explicar conceitos estatísticos, orientar a elaboração e revisão de código Python com Pandas e Matplotlib, discutir tratamentos de dados e valores atípicos, sugerir gráficos, auxiliar na documentação e orientar procedimentos com Git e GitHub.

**Verificações realizadas pelo candidato:** execução dos códigos em Python 3.12, conferência das saídas e dos indicadores estatísticos, inspeção dos gráficos, investigação de valores atípicos e teste da versão inicial a partir de uma cópia clonada do repositório com ambiente virtual independente. A versão ampliada foi executada integralmente no ambiente local.

As interpretações são apresentadas com as limitações identificadas. A utilização da ferramenta não implica que ela tenha verificado externamente a veracidade dos anúncios. A obtenção direta do dataset pelo link do Kaggle continua sem um novo teste de download nesta auditoria.

## 10. Estado do projeto

Análise exploratória executada e documentada, com seis gráficos gerados. A versão inicial teve reprodutibilidade testada em ambiente independente utilizando uma cópia local do dataset; a versão ampliada passou por execução integral no ambiente de desenvolvimento. Projeto em revisão final para submissão à Etapa 2 do processo seletivo SYNAPTA 2026.
