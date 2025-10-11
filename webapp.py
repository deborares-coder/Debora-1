import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# CONFIGURAÇÃO DO APP
# =====================================================
st.set_page_config(
    page_title="Distribuição dos recursos do FUNDEB (Fundo de Manutenção e Desenvolvimento da Educação Básica e de Valorização dos Profissionais da Educação)",
    page_icon="📊",
    layout="wide"
)

# Estilo customizado para deixar o app moderno
st.markdown("""
<style>
    .big-font {
        font-size:28px !important;
        font-weight: bold;
        color: #2E86C1;
    }
    .metric-container {
        background-color: #F8F9F9;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# =====================================================
# CABEÇALHO
# =====================================================
st.title("📊 Distribuição dos recursos do FUNDEB")
st.markdown("<p class='big-font'>Por: Débora Resende Maranhão</p>", unsafe_allow_html=True)
st.markdown("---")

# =====================================================
# OBJETIVO
# =====================================================
st.header("🎯 Objetivo do App")
st.info("""
O presente aplicativo tem como objetivo **consultar e visualizar** informações sobre a distribuição do **FUNDEB** no Brasil.  

O **FUNDEB** é o principal fonte de financiamento da educação básica, e o **MEC** publica portarias trimestrais que detalham:
- Recursos recebidos por estado/município/rede de ensino;
- Complementações da União(VAAF, VAAT e VAAR);
- Matrículas ponderadas por município;
- Distribuição consolidada final.  

Este app é um **protótipo interativo** para simular como essas informações podem ser apresentadas de forma visual e acessível.
""")

st.markdown("---")

dados = {
    "ANO": ["2022", "2022", "2022", "2022"],
    "Estado": ["ES", "MG", "BA", "SP"],
    "Matrículas ponderadas": [82000, 145000, 132000, 210000],
    "Complementação VAAF(R$ mi)": [2000, 45000, 13000, 2100],
    "Complementação VAAR(R$ mi)": [0, 5000, 12000, 360000],
    "Valor FUNDEB (R$ mi)": [84000, 195000, 157000, 7200]
}

df = pd.DataFrame(dados)

st.subheader("📊 Distribuição de Recursos (Exemplo)")
st.dataframe(df)
# =====================================================
# DEMONSTRAÇÃO COM DADOS FUNCIONAIS
# =====================================================
st.header("🖥️ Demonstração Interativa")

# Colunas de seleção sem gerar barras brancas
col1, col2 = st.columns(2)
with col1:
    municipio = st.selectbox("🏙️ Selecione o Município:", 
                             ["Fortaleza", "São Paulo", "Salvador", "Belo Horizonte"])
with col2:
    ano = st.selectbox("📅 Selecione o Ano:", [2022, 2023, 2024])

# Dados simulados para teste funcional
dados_demo = {
    # Fortaleza
    ("Fortaleza", 2022): {"matriculas": 340000, "valor": 2350000000},
    ("Fortaleza", 2023): {"matriculas": 350000, "valor": 2450000000},
    ("Fortaleza", 2024): {"matriculas": 360000, "valor": 2550000000},
    # São Paulo
    ("São Paulo", 2022): {"matriculas": 1150000, "valor": 9400000000},
    ("São Paulo", 2023): {"matriculas": 1200000, "valor": 9800000000},
    ("São Paulo", 2024): {"matriculas": 1250000, "valor": 10200000000},
    # Salvador
    ("Salvador", 2022): {"matriculas": 400000, "valor": 2800000000},
    ("Salvador", 2023): {"matriculas": 420000, "valor": 2950000000},
    ("Salvador", 2024): {"matriculas": 440000, "valor": 3100000000},
    # Belo Horizonte
    ("Belo Horizonte", 2022): {"matriculas": 300000, "valor": 2000000000},
    ("Belo Horizonte", 2023): {"matriculas": 310000, "valor": 2100000000},
    ("Belo Horizonte", 2024): {"matriculas": 320000, "valor": 2200000000},
}

resultado = dados_demo.get((municipio, ano), {"matriculas": "N/D", "valor": "N/D"})

# Exibir métricas em cards estilizados
colA, colB = st.columns(2)
with colA:
    st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
    matriculas_fmt = f"{resultado['matriculas']:,}".replace(",", ".") if isinstance(resultado['matriculas'], int) else resultado['matriculas']
    st.metric("Número de Matrículas", matriculas_fmt)
    st.markdown("</div>", unsafe_allow_html=True)

with colB:
    st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
    valor_fmt = f"R$ {resultado['valor']:,}".replace(",", ".") if isinstance(resultado['valor'], int) else resultado['valor']
    st.metric("Valor Recebido", valor_fmt)
    st.markdown("</div>", unsafe_allow_html=True)

st.info("⚠️ Obs: Estes valores são **simulações fictícias**. Futuramente serão substituídos pelos dados oficiais do MEC.")

# =====================================================
# VISUALIZAÇÃO GRÁFICA
# =====================================================
st.header("📈 Visualização dos Dados (Fictícios)")

df_demo = pd.DataFrame([
    {"Município": "Fortaleza", "Ano": 2022, "Matrículas": 340000, "Valor": 2350000},
    {"Município": "Fortaleza", "Ano": 2023, "Matrículas": 350000, "Valor": 2450000},
    {"Município": "Fortaleza", "Ano": 2024, "Matrículas": 360000, "Valor": 2550000},
    {"Município": "São Paulo", "Ano": 2022, "Matrículas": 1150000, "Valor": 9400000},
    {"Município": "São Paulo", "Ano": 2023, "Matrículas": 1200000, "Valor": 9800000},
    {"Município": "São Paulo", "Ano": 2024, "Matrículas": 1250000, "Valor": 10200000},
    {"Município": "Salvador", "Ano": 2022, "Matrículas": 400000, "Valor": 2800000},
    {"Município": "Salvador", "Ano": 2023, "Matrículas": 420000, "Valor": 2950000},
    {"Município": "Salvador", "Ano": 2024, "Matrículas": 440000, "Valor": 3100000},
    {"Município": "Belo Horizonte", "Ano": 2022, "Matrículas": 300000, "Valor": 2000000},
    {"Município": "Belo Horizonte", "Ano": 2023, "Matrículas": 310000, "Valor": 2100000},
    {"Município": "Belo Horizonte", "Ano": 2024, "Matrículas": 320000, "Valor": 2200000},
])

fig = px.bar(df_demo, x="Município", y="Valor", color="Ano", barmode="group",
             labels={"Valor": "Valor Recebido (R$)", "Município": "Cidade", "Ano": "Ano"},
             title="Distribuição Fictícia de Recursos FUNDEB 2022-2024")

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================================
# CONCLUSÃO
# =====================================================
st.header("✅ Conclusão")
st.success("""
Este app é um **protótipo inicial** que já mostra:
- Layout moderno e interativo;
- Seleção dinâmica de município/estado e ano;
- Indicadores em destaque (cards);
- Gráfico interativo com Plotly mostrando todos os anos.

As próximas etapas incluirão:
- Integração com dados reais do MEC;
- Mapas interativos (geolocalização);
- Exportação de relatórios em PDF/Excel.

Dessa forma, será possível **facilitar a análise da distribuição dos recursos** e apoiar a gestão educacional em estados e municípios.
""")



