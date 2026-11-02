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

## 7. Aluguel por metro quadrado e sensibilidade à área
A análise do aluguel por metro quadrado considerou **11.655 imóveis com área positiva**, obtendo média geral de **R$ 46,69/m²** e mediana de **R$ 37,50/m²**.

A comparação por tipo de imóvel revelou diferenças relevantes. Os **studios e kitnets** apresentaram a maior média (R$ 72,74/m²) e a maior mediana (R$ 61,11/m²). As **casas em condomínio** registraram a segunda maior média (R$ 68,29/m²), mas sua mediana foi de apenas R$ 31,25/m², indicando uma diferença expressiva entre os dois indicadores. Os apartamentos apresentaram média de R$ 48,47/m² e mediana de R$ 41,58/m².

As casas apresentaram os menores valores por metro quadrado, com média de R$ 27,70/m² e mediana de R$ 24,74/m².

### Sensibilidade aos registros de áreas pequenas
Foram identificados **quatro imóveis com áreas inferiores a 5 m²**, incluindo uma casa em condomínio no Jardim dos Estados com quatro quartos, três vagas de garagem e apenas 1 m² de área declarada, indicando possível inconsistência cadastral.

A exclusão experimental desses quatro registros reduziu a média geral de **R$ 46,69/m² para R$ 45,65/m²**, uma diferença aproximada de 2,23%, mantendo a mediana em R$ 37,50/m².

Ao considerar somente imóveis com área de pelo menos 20 m², a média passou para **R$ 44,94/m²** e a mediana para **R$ 37,29/m²**.

**Conclusão:** o aluguel por metro quadrado apresenta diferenças importantes entre os tipos de imóveis. Studios e kitnets registraram os maiores valores típicos por m², enquanto casas apresentaram os menores. A comparação também demonstrou que médias podem ser influenciadas por observações extremas, especialmente na categoria de casas em condomínio.

**Decisão metodológica:** manter os 11.655 imóveis com área positiva na análise principal e utilizar limites mínimos de área para avaliar a sensibilidade dos resultados, sem excluir definitivamente registros suspeitos.

**Limitação:** os resultados são descritivos e não controlam simultaneamente localização, área, conservação e outras características. Também não foi possível verificar os anúncios originais para confirmar eventuais inconsistências cadastrais. Portanto, a média geral por m² não deve ser interpretada como um preço de referência aplicável a todos os imóveis de São Paulo.

## 8. Comparação dos aluguéis por tipo de imóvel

A análise dos 11.657 anúncios identificou quatro categorias de imóveis: apartamentos (7.194 registros), casas (2.841), studios e kitnets (1.381) e casas em condomínio (241).

As casas em condomínio apresentaram o maior aluguel médio, de **R$ 3.912,55**, mas sua mediana foi de **R$ 2.200,00**, inferior à mediana de casas e apartamentos. Os studios e kitnets apresentaram os menores valores de média (R$ 2.127,83) e mediana (R$ 1.850,00).

Entretanto, a interpretação desses resultados exige cautela devido às diferenças entre os tamanhos das amostras e à presença de valores elevados, especialmente na categoria de casas em condomínio.

Nessa categoria, foram identificados nove anúncios com aluguel de R$ 15.000,00. A retirada experimental dos cinco maiores registros reduziu a média de R$ 3.912,55 para R$ 3.677,65, aproximadamente **6%**, enquanto a mediana permaneceu em R$ 2.200,00.

**Conclusão:** os dados revelam diferenças descritivas nos valores anunciados entre os quatro tipos de imóveis. Contudo, a maior média observada nas casas em condomínio deve ser interpretada com cautela, pois é influenciada por anúncios de valores elevados e foi calculada a partir de uma amostra menor que a das demais categorias.

**Limitação:** os tamanhos das amostras são diferentes, não foram realizados testes inferenciais para avaliar a incerteza das comparações e não houve controle simultâneo de fatores como localização, área e número de quartos. Portanto, os resultados não permitem afirmar que o tipo de imóvel, isoladamente, explique as diferenças observadas nos aluguéis.

## 9. Resposta à pergunta orientadora

**Quais características parecem acompanhar os maiores e os menores preços de aluguel e o que os dados não permitem concluir?**

A análise dos 11.657 anúncios identificou associações entre os aluguéis anunciados e características dos imóveis, especialmente **área, número de quartos, tipo de imóvel e localidade**.

A metragem apresentou associação linear positiva com o aluguel (Pearson = **0,667**). Também foi observada uma tendência geral de aluguéis mais elevados em anúncios de imóveis com mais quartos.

As médias de aluguel apresentaram diferenças expressivas entre localidades. Considerando aquelas com pelo menos 30 anúncios, Jardim Leonor apresentou a maior média, enquanto Taboão apresentou a menor.

O tipo de imóvel também esteve associado a diferenças nos valores anunciados. As casas em condomínio apresentaram o maior aluguel médio entre as quatro categorias, enquanto studios e kitnets apresentaram a menor média. Ao comparar o aluguel por m², porém, studios e kitnets apresentaram a maior mediana (R$ 61,11/m²), demonstrando que os rankings dependem da medida utilizada.

Entretanto, o ranking das localidades mudou quando o limite mínimo de anúncios passou de 20 para 30 ou 50, demonstrando a importância das decisões metodológicas. Além disso, as comparações descritivas não controlaram simultaneamente localização, área, tipo de imóvel, conservação e outros fatores potencialmente relevantes.

**Síntese:** os resultados permitem concluir que, na amostra analisada, características como área, quantidade de quartos, tipo de imóvel e localização estão associadas aos valores anunciados de aluguel. Imóveis maiores e com mais quartos geralmente apresentaram preços mais elevados, enquanto determinadas localidades e categorias registraram médias superiores às demais.

Essas conclusões são sustentadas pelos dados analisados. Contudo, os métodos empregados não permitem determinar o efeito isolado de cada característica nem estabelecer relações de causa e efeito. Os resultados também não devem ser automaticamente generalizados para todo o mercado imobiliário de São Paulo, pois se referem aos anúncios presentes no dataset, e não necessariamente aos valores efetivamente negociados.
