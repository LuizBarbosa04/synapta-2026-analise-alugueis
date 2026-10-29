"""Dashboard interativo da análise exploratória de aluguéis — SYNAPTA 2026.

Execute com: python -m streamlit run dashboard.py
O arquivo data.csv é mantido localmente, na mesma pasta.
"""

from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="SYNAPTA 2026 | Aluguéis em São Paulo",
    page_icon="🏠",
    layout="wide",
)

PASTA_PROJETO = Path(__file__).resolve().parent
CAMINHO_DADOS = PASTA_PROJETO / "data.csv"
LIMITES_AREA = [1, 5, 10, 15, 20]
LIMITES_LOCALIDADE = [20, 30, 50]


def formatar_numero(valor, casas=2):
    """Formata números no padrão brasileiro."""
    texto = f"{valor:,.{casas}f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_moeda(valor):
    return f"R$ {formatar_numero(valor)}"


@st.cache_data
def carregar_dados(caminho, ultima_modificacao):
    """Carrega os dados. A data de modificação invalida o cache ao trocar o CSV."""
    dados = pd.read_csv(caminho)
    colunas = {"address", "district", "area", "bedrooms", "garage", "type", "rent", "total"}
    faltantes = sorted(colunas - set(dados.columns))
    if faltantes:
        raise ValueError("Colunas ausentes no CSV: " + ", ".join(faltantes))
    for coluna in ["area", "bedrooms", "garage", "rent", "total"]:
        dados[coluna] = pd.to_numeric(dados[coluna], errors="coerce")
    return dados


st.title("🏠 Análise de Aluguéis em São Paulo")
st.caption("Desafio SYNAPTA 2026 — Etapa 2 | Dashboard exploratório")

if not CAMINHO_DADOS.is_file():
    st.error(
        "Arquivo data.csv não encontrado. Baixe o dataset indicado no README "
        "e coloque-o na mesma pasta de dashboard.py."
    )
    st.stop()

try:
    df = carregar_dados(str(CAMINHO_DADOS), CAMINHO_DADOS.stat().st_mtime_ns)
except Exception as erro:
    st.error(f"Falha ao carregar o dataset: {erro}")
    st.stop()

# O filtro principal é compartilhado entre as três primeiras abas.
st.sidebar.header("Filtros")
tipos_disponiveis = sorted(df["type"].dropna().unique().tolist())
tipos_selecionados = st.sidebar.multiselect(
    "Tipos de imóveis",
    options=tipos_disponiveis,
    default=tipos_disponiveis,
)
df_filtrado = df.loc[df["type"].isin(tipos_selecionados)].copy()
st.sidebar.caption(
    "Os filtros por tipo afetam Visão geral, Localidades e Aluguel por m². "
    "Qualidade dos dados usa a base completa."
)

aba_geral, aba_localidades, aba_m2, aba_qualidade = st.tabs(
    ["📊 Visão geral", "📍 Localidades", "📐 Aluguel por m²", "🛡️ Qualidade dos dados"]
)

# ==================================================
# ABA 1 — VISAO GERAL
# ==================================================
with aba_geral:
    st.subheader("Indicadores dos imóveis selecionados")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total de anúncios", formatar_numero(len(df_filtrado), 0))
    c2.metric(
        "Aluguel médio",
        formatar_moeda(df_filtrado["rent"].mean()) if not df_filtrado.empty else "—",
    )
    c3.metric(
        "Aluguel mediano",
        formatar_moeda(df_filtrado["rent"].median()) if not df_filtrado.empty else "—",
    )
    c4.metric("Tipos de imóveis", df_filtrado["type"].nunique())

    if df_filtrado.empty:
        st.warning("Selecione pelo menos um tipo de imóvel na barra lateral.")
    else:
        resumo_tipos = (
            df_filtrado.groupby("type")["rent"]
            .agg(quantidade="count", media="mean", mediana="median")
            .sort_values("media", ascending=False)
        )
        st.subheader("Média e mediana por tipo de imóvel")
        st.bar_chart(
            resumo_tipos[["media", "mediana"]],
            x_label="Tipo de imóvel",
            y_label="Aluguel anunciado (R$)",
            stack=False
        )
        st.dataframe(
            resumo_tipos.reset_index(),
            hide_index=True,
            width="stretch",
            column_config={
                "type": "Tipo de imóvel",
                "quantidade": "Anúncios",
                "media": st.column_config.NumberColumn("Média", format="R$ %.2f"),
                "mediana": st.column_config.NumberColumn("Mediana", format="R$ %.2f"),
            },
        )
        st.caption("Os dados são anúncios, não preços de contratos efetivamente firmados.")

# ==================================================
# ABA 2 — LOCALIDADES
# ==================================================
with aba_localidades:
    st.subheader("Ranking de aluguéis por localidade")
    limite_anuncios = st.select_slider(
        "Mínimo de anúncios por localidade",
        options=LIMITES_LOCALIDADE,
        value=30,
        key="limite_localidade",
    )
    if df_filtrado.empty:
        st.warning("Selecione pelo menos um tipo de imóvel na barra lateral.")
    else:
        localidades = (
            df_filtrado.groupby("district")["rent"]
            .agg(quantidade="count", media="mean", mediana="median")
        )
        localidades_validas = localidades.loc[
            localidades["quantidade"] >= limite_anuncios
        ].sort_values("media", ascending=False)
        if localidades_validas.empty:
            st.info("Nenhuma localidade atende ao limite selecionado.")
        else:
            top10 = localidades_validas.head(10).reset_index()
            st.metric("Localidades incluídas", len(localidades_validas))
            st.bar_chart(
                top10,
                x="district",
                y="media",
                sort=False,
                x_label="Localidade (maior média primeiro)",
                y_label="Aluguel médio (R$)",
            )
            st.dataframe(
                top10,
                hide_index=True,
                width="stretch",
                column_config={
                    "district": "Localidade",
                    "quantidade": "Anúncios",
                    "media": st.column_config.NumberColumn("Média", format="R$ %.2f"),
                    "mediana": st.column_config.NumberColumn("Mediana", format="R$ %.2f"),
                },
            )
    st.caption(
        "O ranking depende do limite e dos tipos selecionados. "
        "Não representa uma classificação definitiva dos bairros de São Paulo."
    )

# ==================================================
# ABA 3 — ALUGUEL POR METRO QUADRADO
# ==================================================
with aba_m2:
    st.subheader("Aluguel por metro quadrado")
    area_minima = st.select_slider(
        "Área mínima considerada",
        options=LIMITES_AREA,
        value=1,
        format_func=lambda valor: f"{valor} m²",
        key="limite_area",
    )
    df_area = df_filtrado.loc[
        (df_filtrado["area"] > 0) & (df_filtrado["area"] >= area_minima)
    ].copy()

    if df_area.empty:
        st.warning("Nenhum imóvel atende aos filtros selecionados.")
    else:
        df_area["aluguel_m2"] = df_area["rent"] / df_area["area"]
        m1, m2, m3 = st.columns(3)
        m1.metric("Imóveis analisados", formatar_numero(len(df_area), 0))
        m2.metric("Média por m²", formatar_moeda(df_area["aluguel_m2"].mean()))
        m3.metric("Mediana por m²", formatar_moeda(df_area["aluguel_m2"].median()))

        st.subheader("Sensibilidade à área mínima")
        cenarios = []
        for limite in LIMITES_AREA:
            valores = df_filtrado.loc[
                (df_filtrado["area"] > 0) & (df_filtrado["area"] >= limite)
            ]
            if not valores.empty:
                aluguel_m2 = valores["rent"] / valores["area"]
                cenarios.append(
                    {
                        "Área mínima": limite,
                        "Imóveis": len(valores),
                        "Média": aluguel_m2.mean(),
                        "Mediana": aluguel_m2.median(),
                    }
                )
        tabela_sensibilidade = pd.DataFrame(cenarios)
        if not tabela_sensibilidade.empty:
            st.line_chart(
                tabela_sensibilidade,
                x="Área mínima",
                y=["Média", "Mediana"],
                x_label="Área mínima (m²)",
                y_label="Aluguel por m² (R$)",
            )
            st.dataframe(
                tabela_sensibilidade,
                hide_index=True,
                width="stretch",
                column_config={
                    "Área mínima": st.column_config.NumberColumn("Área mínima (m²)", format="%d"),
                    "Imóveis": "Imóveis",
                    "Média": st.column_config.NumberColumn("Média (R$/m²)", format="R$ %.2f"),
                    "Mediana": st.column_config.NumberColumn("Mediana (R$/m²)", format="R$ %.2f"),
                },
            )
    st.caption(
        "Os limites são cenários exploratórios. A base original permanece inalterada; "
        "áreas extremamente pequenas podem causar valores por m² pouco plausíveis."
    )

# ==================================================
# ABA 4 — QUALIDADE DOS DADOS (SEMPRE NA BASE COMPLETA)
# ==================================================
with aba_qualidade:
    st.subheader("Qualidade dos dados e limitações")
    faltantes = int(df.isna().sum().sum())
    duplicados = int(df.duplicated().sum())
    areas_zero = int((df["area"] == 0).sum())
    areas_pequenas = int(((df["area"] > 0) & (df["area"] < 5)).sum())

    q1, q2, q3, q4 = st.columns(4)
    q1.metric("Valores ausentes", formatar_numero(faltantes, 0))
    q2.metric("Linhas duplicadas", formatar_numero(duplicados, 0))
    q3.metric("Área igual a zero", formatar_numero(areas_zero, 0))
    q4.metric("Área entre 0 e 5 m²", formatar_numero(areas_pequenas, 0))

    st.markdown("#### Registros com área positiva inferior a 5 m²")
    suspeitos = df.loc[(df["area"] > 0) & (df["area"] < 5)].copy()
    if suspeitos.empty:
        st.info("Não foram identificados registros nesse intervalo.")
    else:
        suspeitos["aluguel_m2"] = suspeitos["rent"] / suspeitos["area"]
        st.dataframe(
            suspeitos[
                ["district", "type", "area", "bedrooms", "garage", "rent", "aluguel_m2"]
            ],
            hide_index=True,
            width="stretch",
        )

    st.markdown("#### Decisões metodológicas")
    st.write(
        "Os dois registros de área zero são preservados nas análises de aluguel "
        "que não dependem de metragem, mas excluídos dos cálculos de aluguel por m² "
        "e da correlação entre área e aluguel."
    )
    st.write(
        "Registros com área positiva muito pequena são sinalizados como potenciais "
        "inconsistências, mas não removidos automaticamente."
    )
    st.info(
        "A análise utiliza preços anunciados, não contratos. "
        "Comparações descritivas não demonstram causalidade nem garantem "
        "representatividade do mercado imobiliário completo."
    )

st.divider()
st.caption(
    "Fonte: Sao Paulo Housing Prices (Kaggle). "
    "Projeto SYNAPTA 2026 — uso educacional e análise exploratória."
)
