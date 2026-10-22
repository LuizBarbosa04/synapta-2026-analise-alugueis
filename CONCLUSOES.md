# Conclusões da Análise Exploratória — SYNAPTA 2026

**Projeto:** Análise exploratória dos preços de aluguel em São Paulo
**Opção escolhida:** 1 — Preços de aluguel em São Paulo

As conclusões a seguir referem-se aos **11.657 anúncios** presentes no dataset analisado. Os resultados descrevem a amostra, sem representar necessariamente todos os imóveis disponíveis para aluguel na cidade.

## 1. Distribuição dos aluguéis

O aluguel médio anunciado foi de **R$ 3.250,81**, enquanto o aluguel mediano foi de **R$ 2.415,00**. A média superior à mediana, juntamente com o histograma, indica uma distribuição assimétrica à direita, com presença de anúncios de valores elevados.

**Limitação:** os valores representam preços anunciados, não necessariamente os efetivamente negociados.

## 2. Diferenças entre localidades

Entre as localidades com **pelo menos 30 anúncios**, Jardim Leonor apresentou o maior aluguel médio (**R$ 7.455,74**, com 38 anúncios) e Taboão apresentou o menor (**R$ 1.473,14**, com 49 anúncios).

**Limitação:** a comparação depende do limite mínimo de anúncios e não controla as diferenças de área, tipo de imóvel e outras características entre localidades.

## 3. Relação entre área e aluguel

A correlação de Pearson entre área e aluguel, calculada somente para os **11.655 registros com área positiva**, foi de **0,667**, indicando associação linear positiva na amostra: imóveis maiores tendem a apresentar aluguéis mais elevados.

**Limitação:** correlação não demonstra causalidade e não significa que a área, isoladamente, determine o preço anunciado.

## 4. Relação entre quartos e aluguel

Observou-se uma tendência geral de aluguéis médios mais elevados em imóveis com maior número de quartos. Por exemplo, anúncios com **1 quarto** apresentaram média de **R$ 2.153,96**, enquanto anúncios com **4 quartos** apresentaram média de **R$ 7.806,27**.

A relação não foi estritamente crescente: o grupo de 6 quartos teve média inferior ao de 5 quartos.

**Limitação:** os tamanhos dos grupos são diferentes; havia 4.193 anúncios com 1 quarto, mas apenas 23 com 6 quartos. As médias não isolam os efeitos da localização, da metragem e do tipo do imóvel.

## 5. Influência de um valor extremo

Foi identificado um studio de **24 m²**, no Planalto Paulista, com aluguel anunciado de **R$ 25.000**. Sua retirada experimental diminuiu a média geral em aproximadamente **0,057%** (R$ 1,87) e a média dos studios em aproximadamente **0,78%** (R$ 16,57).

A decisão foi **preservar o registro na análise principal**, pois não existe evidência suficiente para afirmar que o valor anunciado esteja incorreto.

**Limitação:** o anúncio não foi verificado externamente. A baixa influência desse registro na média geral não significa que outros valores extremos sejam irrelevantes.

## 6. Análise de sensibilidade do critério por localidade

Para avaliar a influência da quantidade mínima de anúncios nos resultados, foram comparados três limites: **20, 30 e 50 registros por localidade**.

| Limite mínimo | Localidades incluídas | Cobertura dos anúncios |
|---|---:|---:|
| 20 anúncios | 131 | 61,10% |
| 30 anúncios | 78 | 50,36% |
| 50 anúncios | 38 | 37,47% |

Os rankings mudaram conforme o limite adotado. Com **20 anúncios**, Alphaville apresentou a maior média; com **30 anúncios**, Jardim Leonor; e com **50 anúncios**, Cerqueira César.

**Decisão metodológica:** manter 30 anúncios como critério principal da comparação exploratória, por equilibrar uma quantidade mínima por grupo com a cobertura de aproximadamente metade da amostra. Esse limite não garante estabilidade nem representatividade estatística.

**Limitação:** as classificações dependem do critério de inclusão e da composição dos anúncios. Não representam um ranking definitivo dos bairros de São Paulo.

## 7. Resposta à pergunta orientadora

**Quais características parecem acompanhar os maiores e os menores preços de aluguel e o que os dados não permitem concluir?**

A análise dos 11.657 anúncios identificou associações entre os aluguéis anunciados e características dos imóveis, especialmente **área, número de quartos e localidade**.

A metragem apresentou associação linear positiva com o aluguel (Pearson = **0,667**). Também foi observada uma tendência geral de aluguéis mais elevados em anúncios de imóveis com mais quartos. As médias de aluguel variaram significativamente entre localidades; entre aquelas com pelo menos 30 anúncios, Jardim Leonor apresentou a maior média e Taboão a menor.

Entretanto, o ranking mudou quando o limite mínimo de anúncios passou de 20 para 30 ou 50, mostrando a importância dessa decisão metodológica. Além disso, as comparações descritivas não controlaram simultaneamente a localização, a área, o tipo de imóvel, a conservação e outros fatores potencialmente relevantes.

**Síntese:** na amostra estudada, imóveis maiores, com mais quartos e em determinadas localidades tendem a apresentar maiores valores anunciados de aluguel. Os dados, porém, **não permitem concluir causalidade**, determinar o efeito isolado de cada característica nem afirmar que os resultados representem todo o mercado imobiliário de São Paulo. Os valores são de anúncios e não necessariamente de contratos negociados.
