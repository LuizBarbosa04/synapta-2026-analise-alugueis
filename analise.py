import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def formatar_numero(valor, casas=2):
    """Formata números com separadores brasileiros."""
    texto = f"{valor:,.{casas}f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")

# Identificar a pasta onde está este arquivo Python
PASTA_PROJETO = Path(__file__).resolve().parent

# Definir os caminhos dos dados e gráficos
CAMINHO_DADOS = PASTA_PROJETO / "data.csv"
pasta_graficos = PASTA_PROJETO / "graficos"

# Garantir a existência da pasta de gráficos
pasta_graficos.mkdir(exist_ok=True)

# Carregar o dataset
df = pd.read_csv(CAMINHO_DADOS)

# Etapa 2 - Preservar a base original
df_geral = df.copy()

# Etapa 3 - Selecionar imóveis com área positiva
df_area_valida = df[df["area"] > 0].copy()

# Etapa 4 - Verificar os resultados
print("Base geral:", len(df_geral))
print("Base com área válida:", len(df_area_valida))
print("Registros desconsiderados:",
      len(df_geral) - len(df_area_valida))


# Registrar a primeira decisão de tratamento
decisao = {
    "Problema": "Imóveis com área igual a zero",
    "Quantidade": len(df_geral) - len(df_area_valida),
    "Decisão": "Filtrar apenas nas análises de área",
    "Justificativa": "Área zero não representa uma metragem válida",
    "Impacto": "Dois registros fora das análises de área"
}

print("\nREGISTRO DE TRATAMENTO")
for campo, valor in decisao.items():
    print(f"{campo}: {valor}")

# Etapa 2.4 - Verificar valores ausentes

print("\nVERIFICAÇÃO DE VALORES AUSENTES")

valores_ausentes = df_geral.isnull().sum()

print(valores_ausentes)

print("\nTotal de valores ausentes:",
      valores_ausentes.sum())

# Etapa 2.5 - Verificar registros duplicados

print("\nVERIFICAÇÃO DE DUPLICADOS")

duplicados = df_geral.duplicated()

quantidade_duplicados = duplicados.sum()

print("Total de registros duplicados:",
      quantidade_duplicados)

if quantidade_duplicados > 0:
    print("\nRegistros duplicados encontrados:")
    print(df_geral[duplicados].head())
else:
    print("Nenhuma linha totalmente duplicada encontrada.")


# Etapa 2.6 - Investigar valores dos aluguéis

print("\nANÁLISE INICIAL DOS ALUGUÉIS")

print(df_geral["rent"].describe())

print("\nOS 5 MAIORES ALUGUÉIS")

maiores_alugueis = df_geral.nlargest(5, "rent")

print(
    maiores_alugueis[
        ["district", "area", "bedrooms", "rent"]
    ].to_string(index=False)
)


# Etapa 2.7 - Investigar o maior aluguel

print("\nINVESTIGAÇÃO DO MAIOR ALUGUEL")

maior_aluguel = df_geral.nlargest(1, "rent")

print(maior_aluguel.to_string(index=False))

# Calcular o preço por metro quadrado
area = maior_aluguel["area"].iloc[0]
aluguel = maior_aluguel["rent"].iloc[0]

if area > 0:
    preco_m2 = aluguel / area
    print(f"\nPreço por m²: R$ {preco_m2:.2f}")


# Etapa 2.8 - Análise de sensibilidade

print("\nIMPACTO DO MAIOR ALUGUEL")

media_original = df_geral["rent"].mean()

# Retirar somente a primeira ocorrência
# do maior aluguel da cópia de análise
indice_maior = df_geral["rent"].idxmax()

df_sem_maior = df_geral.drop(index=indice_maior)

media_sem_maior = df_sem_maior["rent"].mean()

diferenca = media_original - media_sem_maior

print(f"Média original: R$ {media_original:.2f}")
print(f"Média sem o maior registro: R$ {media_sem_maior:.2f}")
print(f"Diferença: R$ {diferenca:.2f}")


# Etapa 2.9 - Comparação entre studios e kitnets

print("\nANÁLISE DE STUDIOS E KITNETS")

studios = df_geral[
    df_geral["type"] == "Studio e kitnet"
].copy()

print("Quantidade de studios:", len(studios))

print("\nEstatísticas dos aluguéis:")
print(studios["rent"].describe())

print("\nOs 5 studios mais caros:")
print(
    studios.nlargest(5, "rent")[
        ["district", "area", "rent"]
    ].to_string(index=False)
)


# Etapa 2.10 - Sensibilidade da média dos studios

print("\nIMPACTO DO MAIOR ALUGUEL NOS STUDIOS")

media_studios = studios["rent"].mean()

# Criar uma cópia sem o registro mais caro
indice_maior_studio = studios["rent"].idxmax()
studios_sem_maior = studios.drop(index=indice_maior_studio)

media_sem_maior = studios_sem_maior["rent"].mean()

diferenca = media_studios - media_sem_maior
impacto_percentual = (diferenca / media_studios) * 100

print(f"Média original: R$ {media_studios:.2f}")
print(f"Média sem o maior studio: R$ {media_sem_maior:.2f}")
print(f"Diferença: R$ {diferenca:.2f}")
print(f"Impacto percentual: {impacto_percentual:.2f}%")

# Etapa 2.11 - Registro automático do valor atípico

impacto_geral = (
    (media_original - df_sem_maior["rent"].mean())
    / media_original
) * 100

registro_outlier = {
    "Problema": "Imóvel com aluguel muito elevado",
    "Localidade": maior_aluguel["district"].iloc[0],
    "Aluguel": (f"R$ {formatar_numero(maior_aluguel['rent'].iloc[0])}"),
    "Área": (f"{formatar_numero(maior_aluguel['area'].iloc[0], 0)} m²"),
    "Decisão": "Preservar na análise principal",
    "Justificativa": (
        "Não há evidência suficiente para "
        "confirmar erro no anúncio"
    ),
    "Impacto geral": (f"Redução de {formatar_numero(impacto_geral, 3)}% na média"),
    "Impacto nos studios": (f"Redução de {formatar_numero(impacto_percentual)}% na média"),
    "Limitação": (
        "A veracidade do valor anunciado "
        "não foi confirmada externamente"
    )
}

print("\nREGISTRO DE VALOR ATÍPICO")

for campo, valor in registro_outlier.items():
    print(f"{campo}: {valor}")

# Etapa 3.1 - Distribuição dos aluguéis

print("\nDISTRIBUIÇÃO DOS ALUGUÉIS")

media = df_geral["rent"].mean()
mediana = df_geral["rent"].median()

plt.figure(figsize=(10, 6))

plt.hist(
    df_geral["rent"],
    bins=40,
    color="steelblue",
    edgecolor="white"
)

plt.axvline(
    media,
    color="red",
    linestyle="--",
    label=f"Média: R$ {media:,.2f}"
)

plt.axvline(
    mediana,
    color="green",
    linestyle="--",
    label=f"Mediana: R$ {mediana:,.2f}"
)

plt.title("Distribuição dos preços de aluguel em São Paulo")
plt.xlabel("Aluguel anunciado (R$)")
plt.ylabel("Quantidade de imóveis")
plt.legend()

plt.tight_layout()

# Salvar o histograma em alta resolução
plt.savefig(
    pasta_graficos / "distribuicao_alugueis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nGráfico salvo com sucesso!")


# Etapa 3.3 - Quantidade de imóveis por localidade

print("\nANÚNCIOS POR LOCALIDADE")

quantidade_bairros = df_geral["district"].value_counts()

print("\n10 localidades com mais anúncios:")
print(quantidade_bairros.head(10))

print("\nTotal de localidades:")
print(df_geral["district"].nunique())

print("\nLocalidades com pelo menos 30 anúncios:")
print((quantidade_bairros >= 30).sum())

print("\nLocalidades com menos de 30 anúncios:")
print((quantidade_bairros < 30).sum())


# Etapa 3.4 - Cobertura das localidades selecionadas

print("\nCOBERTURA DAS LOCALIDADES")

bairros_validos = quantidade_bairros[
    quantidade_bairros >= 30
].index

df_bairros_validos = df_geral[
    df_geral["district"].isin(bairros_validos)
].copy()

quantidade = len(df_bairros_validos)
total = len(df_geral)

percentual = (quantidade / total) * 100

print("Anúncios nas localidades selecionadas:", quantidade)
print("Total de anúncios:", total)
print(f"Cobertura da análise: {percentual:.2f}%")


# Etapa 3.5 - Preços médios por localidade

print("\nANÁLISE DOS ALUGUÉIS POR LOCALIDADE")

resumo_bairros = (
    df_bairros_validos
    .groupby("district")
    .agg(
        quantidade=("rent", "count"),
        aluguel_medio=("rent", "mean"),
        aluguel_mediano=("rent", "median")
    )
    .sort_values("aluguel_medio", ascending=False)
)

print("\n5 LOCALIDADES COM MAIORES ALUGUÉIS MÉDIOS")

print(
    resumo_bairros.head(5).round(2).to_string()
)

print("\n5 LOCALIDADES COM MENORES ALUGUÉIS MÉDIOS")

print(
    resumo_bairros.tail(5)
    .sort_values("aluguel_medio")
    .round(2)
    .to_string()
)



# Etapa 3.7 - Gráfico aprimorado por localidade

maiores = resumo_bairros.head(5)
menores = resumo_bairros.tail(5)

comparacao = pd.concat([maiores, menores])
comparacao = comparacao.sort_values("aluguel_medio")

cores = [
    "steelblue" if bairro in menores.index else "darkorange"
    for bairro in comparacao.index
]

fig, ax = plt.subplots(figsize=(12, 7))

barras = ax.barh(
    comparacao.index,
    comparacao["aluguel_medio"],
    color=cores
)

# Adicionar valor médio e quantidade de anúncios
for barra, (_, linha) in zip(
    barras, comparacao.iterrows()
):
    valor = linha["aluguel_medio"]
    quantidade = int(linha["quantidade"])

    ax.text(
        valor + 100,
        barra.get_y() + barra.get_height() / 2,
        f"R$ {valor:,.0f} (n={quantidade})",
        va="center",
        fontsize=9
    )

ax.set_title(
    "Maiores e menores aluguéis médios por localidade"
)
ax.set_xlabel("Aluguel médio anunciado (R$)")
ax.set_ylabel("Localidade")

# Reservar espaço para os rótulos
ax.set_xlim(
    0,
    comparacao["aluguel_medio"].max() * 1.35
)

fig.text(
    0.5, 0.01,
    "Apenas localidades com pelo menos 30 anúncios. "
    "n = quantidade de anúncios.",
    ha="center",
    fontsize=9
)

fig.tight_layout(rect=[0, 0.04, 1, 1])

fig.savefig(
    pasta_graficos / "aluguel_medio_localidades.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Gráfico aprimorado salvo com sucesso!")


# Etapa 3.8 - Relação entre área e aluguel

print("\nANÁLISE DA RELAÇÃO ENTRE ÁREA E ALUGUEL")

# Utilizar somente imóveis com área positiva
dados_area = df_area_valida.copy()

# Calcular correlação
correlacao = dados_area["area"].corr(
    dados_area["rent"]
)

print(f"Correlação de Pearson: {correlacao:.3f}")

# Criar gráfico de dispersão
plt.figure(figsize=(10, 6))

plt.scatter(
    dados_area["area"],
    dados_area["rent"],
    alpha=0.25,
    s=12,
    color="steelblue"
)

plt.title("Relação entre área e aluguel em São Paulo")
plt.xlabel("Área do imóvel (m²)")
plt.ylabel("Aluguel anunciado (R$)")

plt.tight_layout()

plt.savefig(
    pasta_graficos / "area_vs_aluguel.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Gráfico de área e aluguel salvo com sucesso!")


# Etapa 3.9 - Relação entre quartos e aluguel

print("\nANÁLISE DE ALUGUEL POR QUANTIDADE DE QUARTOS")

resumo_quartos = (
    df_geral
    .groupby("bedrooms")
    .agg(
        quantidade=("rent", "count"),
        aluguel_medio=("rent", "mean"),
        aluguel_mediano=("rent", "median")
    )
    .sort_index()
)

print(resumo_quartos.round(2).to_string())


# Etapa 3.10 - Gráfico de aluguel por quartos

print("\nGERANDO GRÁFICO POR QUANTIDADE DE QUARTOS")

fig, ax = plt.subplots(figsize=(10, 6))

barras = ax.bar(
    resumo_quartos.index.astype(str),
    resumo_quartos["aluguel_medio"],
    color="steelblue"
)

for barra, (_, linha) in zip(
    barras, resumo_quartos.iterrows()
):
    altura = barra.get_height()
    quantidade = int(linha["quantidade"])

    ax.text(
        barra.get_x() + barra.get_width() / 2,
        altura + 150,
        f"n={quantidade}",
        ha="center",
        fontsize=9
    )

ax.set_title("Aluguel médio por quantidade de quartos")
ax.set_xlabel("Quantidade de quartos")
ax.set_ylabel("Aluguel médio anunciado (R$)")

ax.set_ylim(
    0,
    resumo_quartos["aluguel_medio"].max() * 1.2
)

fig.tight_layout()

fig.savefig(
    pasta_graficos / "aluguel_por_quartos.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Gráfico por quantidade de quartos salvo!")


# Etapa 5.10 - Sensibilidade ao limite de anúncios

print("\nSENSIBILIDADE AO LIMITE DE ANÚNCIOS")

for limite in [20, 30, 50]:

    contagem = df_geral["district"].value_counts()

    localidades_validas = contagem[
        contagem >= limite
    ].index

    dados_filtrados = df_geral[
        df_geral["district"].isin(localidades_validas)
    ]

    medias = (
        dados_filtrados
        .groupby("district")["rent"]
        .mean()
        .sort_values(ascending=False)
    )

    cobertura = len(dados_filtrados) / len(df_geral) * 100

    print(f"\nLIMITE: {limite} ANÚNCIOS")
    print("Localidades:", len(localidades_validas))
    print(f"Cobertura: {cobertura:.2f}%")

    print("\n3 maiores médias:")
    print(medias.head(3).round(2))

    print("\n3 menores médias:")
    print(medias.tail(3).sort_values().round(2))
# Etapa 6.1 - Analise do aluguel por metro quadrado

print("\nANÁLISE DO ALUGUEL POR METRO QUADRADO")

# Criar uma cópia somente com áreas positivas
df_preco_m2 = df_area_valida.copy()

# Calcular o aluguel por metro quadrado
df_preco_m2["aluguel_m2"] = (
    df_preco_m2["rent"] / df_preco_m2["area"]
)

# Conferir a quantidade de registros
print("Imóveis analisados:", len(df_preco_m2))

# Estatísticas do aluguel por m²
print("\nEstatísticas do aluguel por m²:")
print(df_preco_m2["aluguel_m2"].describe().round(2))

# Identificar os 5 maiores preços por m²
print("\n5 MAIORES ALUGUÉIS POR M²")

print(
    df_preco_m2.nlargest(5, "aluguel_m2")[
        ["district", "type", "area", "rent", "aluguel_m2"]
    ].round(2).to_string(index=False)
)


# Etapa 6.2 - Sensibilidade ao limite minimo de area

print("\nSENSIBILIDADE DO ALUGUEL POR M² À ÁREA MÍNIMA")

for area_minima in [1, 5, 10, 15, 20]:
    df_teste = df_preco_m2[
        df_preco_m2["area"] >= area_minima
    ]

    print(f"\nÁrea mínima: {area_minima} m²")
    print("Quantidade de imóveis:", len(df_teste))
    print(
        "Média do aluguel/m²:",
        round(df_teste["aluguel_m2"].mean(), 2)
    )
    print(
        "Mediana do aluguel/m²:",
        round(df_teste["aluguel_m2"].median(), 2)
    )
    print(
        "Maior aluguel/m²:",
        round(df_teste["aluguel_m2"].max(), 2)
    )
# Etapa 6.3 - Investigacao de areas inferiores a 5 m²

print("\nINVESTIGAÇÃO DE IMÓVEIS COM ÁREA INFERIOR A 5 M²")

imoveis_area_muito_pequena = df_preco_m2[
    df_preco_m2["area"] < 5
].copy()

print("Quantidade de registros:", len(imoveis_area_muito_pequena))

colunas_investigacao = [
    "district",
    "type",
    "area",
    "bedrooms",
    "garage",
    "rent",
    "total",
    "aluguel_m2"
]

print(
    imoveis_area_muito_pequena[colunas_investigacao]
    .round(2)
    .to_string(index=False)
)

# Etapa 6.4 - Comparacao entre aluguel total e aluguel por m²

print("\nCOMPARAÇÃO: ALUGUEL TOTAL X ALUGUEL POR M²")

print("\n5 maiores aluguéis totais:")
print(
    df_preco_m2.nlargest(5, "rent")[
        ["district", "type", "area", "rent", "aluguel_m2"]
    ].round(2).to_string(index=False)
)

print("\n5 maiores aluguéis por m²:")
print(
    df_preco_m2.nlargest(5, "aluguel_m2")[
        ["district", "type", "area", "rent", "aluguel_m2"]
    ].round(2).to_string(index=False)
)

# Etapa 6.5 - Grafico de sensibilidade do aluguel por m²

limites_area = [1, 5, 10, 15, 20]
medias_m2 = []
medianas_m2 = []

for limite in limites_area:
    dados_filtrados = df_preco_m2[
        df_preco_m2["area"] >= limite
    ]

    medias_m2.append(
        dados_filtrados["aluguel_m2"].mean()
    )

    medianas_m2.append(
        dados_filtrados["aluguel_m2"].median()
    )

plt.figure(figsize=(9, 5))

plt.plot(
    limites_area,
    medias_m2,
    marker="o",
    label="Média"
)

plt.plot(
    limites_area,
    medianas_m2,
    marker="s",
    label="Mediana"
)

plt.title("Sensibilidade do aluguel por m² à área mínima")
plt.xlabel("Área mínima considerada (m²)")
plt.ylabel("Aluguel por m² (R$)")
plt.xticks(limites_area)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(
    pasta_graficos / "sensibilidade_aluguel_m2.png",
    dpi=150
)

plt.close()

print("\nGráfico de sensibilidade do aluguel/m² salvo.")

# Etapa 7.1 - Analise por tipo de imovel

print("\nANÁLISE DOS ALUGUÉIS POR TIPO DE IMÓVEL")

resumo_tipos = (
    df.groupby("type")["rent"]
    .agg(
        quantidade="count",
        media="mean",
        mediana="median"
    )
    .sort_values("quantidade", ascending=False)
)

print(resumo_tipos.round(2).to_string())

print("\nQuantidade de tipos de imóvel:")
print(df["type"].nunique())

# Etapa 7.2 - Investigacao das casas em condominio

print("\nINVESTIGAÇÃO: CASAS EM CONDOMÍNIO")

casas_condominio = df[
    df["type"] == "Casa em condomínio"
].copy()

print("\nEstatísticas dos aluguéis:")
print(casas_condominio["rent"].describe().round(2))

print("\n5 maiores aluguéis de casas em condomínio:")

print(
    casas_condominio.nlargest(5, "rent")[
        ["district", "area", "bedrooms", "garage", "rent"]
    ].to_string(index=False)
)

print("\nComparação entre média e mediana:")
print("Média:", round(casas_condominio["rent"].mean(), 2))
print("Mediana:", round(casas_condominio["rent"].median(), 2))


# Etapa 7.3 - Sensibilidade da media das casas em condominio

print("\nSENSIBILIDADE: CASAS EM CONDOMÍNIO")

media_original = casas_condominio["rent"].mean()

# Retirada experimental dos cinco maiores registros
indices_top5 = casas_condominio.nlargest(5, "rent").index

casas_sem_top5 = casas_condominio.drop(
    index=indices_top5
)

media_sem_top5 = casas_sem_top5["rent"].mean()

diferenca = media_original - media_sem_top5
variacao_percentual = (diferenca / media_original) * 100

print("Quantidade original:", len(casas_condominio))
print("Quantidade sem os cinco maiores:", len(casas_sem_top5))

print("Média original:", round(media_original, 2))
print("Média sem os cinco maiores:", round(media_sem_top5, 2))
print("Diferença:", round(diferenca, 2))
print("Redução percentual:", round(variacao_percentual, 2))

print(
    "Mediana sem os cinco maiores:",
    round(casas_sem_top5["rent"].median(), 2)
)

print(
    "Quantidade de anúncios com aluguel de R$ 15.000:",
    (casas_condominio["rent"] == 15000).sum()
)

# Etapa 7.4 - Grafico de aluguel por tipo de imovel

print("\nGERANDO GRÁFICO DE ALUGUEL POR TIPO DE IMÓVEL")

resumo_grafico = resumo_tipos.copy()

posicoes = range(len(resumo_grafico))
largura = 0.35

plt.figure(figsize=(11, 6))

plt.bar(
    [p - largura / 2 for p in posicoes],
    resumo_grafico["media"],
    width=largura,
    label="Média"
)

plt.bar(
    [p + largura / 2 for p in posicoes],
    resumo_grafico["mediana"],
    width=largura,
    label="Mediana"
)

rotulos = [
    f"{tipo}\n(n={quantidade})"
    for tipo, quantidade in zip(
        resumo_grafico.index,
        resumo_grafico["quantidade"]
    )
]

plt.xticks(
    list(posicoes),
    rotulos,
    fontsize=9
)

plt.title("Aluguel médio e mediano por tipo de imóvel")
plt.ylabel("Aluguel anunciado (R$)")
plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    pasta_graficos / "aluguel_por_tipo_imovel.png",
    dpi=150
)

plt.close()

print("Gráfico de aluguel por tipo de imóvel salvo.")
