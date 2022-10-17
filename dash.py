from lxml import html
import requests
import pandas as pd
import numpy as np
import streamlit as st  # 🎈 data web app development
import time  
import plotly.express as px  # interactive charts

moedas = [
"ripple", 
"cosmos", 
"algorand", 
"celo", 
"the-sandbox", 
"kava", 
"stellar", 
"compound-governance-token", 
"nexo", 
"matic-network", 
"theta-token", 
"havven", 
"uniswap", 
"curve-dao-token", 
"polkadot", 
"solana", 
"optimism", 
"bitcoin", 
"lido-dao", 
"gmx", 
"chiliz", 
"tron", 
"ethereum", 
"near", 
"enjincoin", 
"cardano", 
"shiba-inu", 
"gala", 
"avalanche-2", 
"ftx-token", 
"neo", 
"kusama", 
"ravencoin", 
"flow", 
"pancakeswap-token"
]
categorias = [
"Pagamento", 
"Layer 0", 
"Layer 1", 
"Layer 1", 
"GameFi", 
"Layer 1", 
"Layer 1", 
"DeFi", 
"Pagamento", 
"Layer 2", 
"Layer 1", 
"Layer 1", 
"DeFi", 
"DeFi", 
"Layer 0", 
"Layer 1", 
"Layer 2", 
"Pagamento", 
"DeFi", 
"DeFi", 
"GameFi", 
"Layer 1", 
"Layer 1", 
"Layer 1", 
"GameFi", 
"Layer 1", 
"Pagamento", 
"GameFi", 
"Layer 1", 
"DeFi", 
"Layer 1", 
"DeFi", 
"Layer 1", 
"Layer 1", 
"DeFi"
]
var1 = []
var2 = []
var3 = []
var4 =[]

def is_what_percent_of(num_a, num_b):
    return ((num_a - num_b) / num_b) * 100

    
st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

def is_what_percent_of(num_a, num_b):
    return ((num_a - num_b) / num_b) * 100
    

@st.experimental_memo
def get_coin_change():
    try:
        for c in moedas:
            
            page = requests.get(f"https://www.coingecko.com/en/coins/{c}")
            tree = html.fromstring(page.content)
            p_7 = tree.xpath('//*[@id="general"]/div[1]/div[1]/div[3]/div[2]/div[3]/span/text()')[0]
            p_30 = tree.xpath('//*[@id="general"]/div[1]/div[1]/div[3]/div[2]/div[5]/span/text()')[0]
            var1.append(p_7)
            var2.append(p_30)
            var3.append(c)

        serie_1 = pd.Series(var1)
        serie_2 = pd.Series(var2)
        serie_3 = pd.Series(var3)
        serie_4 = np.array(categorias)

        frame = { '7d': serie_1,
        '30d': serie_2,'moeda':serie_3,'cat':serie_4}

        result = pd.DataFrame(frame)
        result['7d'] = result['7d'].str.rstrip('%').astype('float') / 100.0
        result['30d'] = result['30d'].str.rstrip('%').astype('float') / 100.0
        result['Moeda_i'] = result['moeda']
        result.set_index('Moeda_i', inplace=True)
        return result
        time.sleep(3)
    except:
        print('error')

df = get_coin_change()

col1, col2, col3 = st.columns([14, 5, 15])
with col2:
    st.image("logo.png", width=200)

st.title("Crypto Overview")


# top-level filters


# creating a single-element container
placeholder = st.empty()

# dataframe filter
destaque_pst_7d = f"{df.loc[df['7d'].idxmax(), 'moeda']}"
destaque_ngt_7d = f"{df.loc[df['7d'].idxmin(), 'moeda']}"
destaque_pst_30d = f"{df.loc[df['30d'].idxmax(), 'moeda']}"
destaque_ngt_30d = f"{df.loc[df['30d'].idxmin(), 'moeda']}"
# near real-time / live feed simulation
for seconds in range(200):
    maior_semana = ('{:,.2%}'.format(df["7d"].max()))
    menor_semana = ('{:,.2%}'.format(df["7d"].min()))
    maior_mes =    ('{:,.2%}'.format(df["30d"].max()))
    menor_mes =    ('{:,.2%}'.format(df["30d"].min()))
    with placeholder.container():
        kpi1, kpi2, kpi3, kpi4 = st.columns(4)
        
        kpi1.metric(
            label=f"Destaque Positivo (7d): {destaque_pst_7d}",
            value=maior_semana
        )
    
        kpi2.metric(
            label=f"Destaque Negativo(7d): {destaque_ngt_7d}",
            value=menor_semana
        )
    
        kpi3.metric(
            label=f"Destaque Positivo(30d): {destaque_pst_30d}",
            value=maior_mes
        )

        kpi4.metric(
            label=f"Destaque Negativo(30d): {destaque_ngt_30d}",
            value=menor_mes
        )



escolha_cat,  = st.columns([1])

with escolha_cat:
    escolher_catego = st.selectbox(
        "Selecione o setor",
        ("Todos", "Pagamento", "DeFi", "Metaverso", "GameFi", "Layer 0", "Layer 1", "Layer 2"),
    )
    if escolher_catego != "Todos":
        df = df[df['cat'] == escolher_catego]


    fig = px.bar(
    data_frame=df, y="7d", x="moeda",
    )
    fig.update_layout(yaxis_tickformat = '.2%', )
    fig.update_traces(marker_color='rgb(223, 208, 134)')
    st.plotly_chart(fig, use_container_width=True)


    fig2 = px.bar(
    data_frame=df, x="moeda", y="30d")
    fig2.update_layout(yaxis_tickformat = '.2%')
    fig.update_traces(marker_color='rgb(223, 208, 134)')
    fig2.update_traces(marker_color='rgb(223, 208, 134)')
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("Cotação Cripto")
    st.dataframe(df)
    time.sleep(1)
