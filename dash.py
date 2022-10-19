#from tkinter import Image
from lxml import html
import requests
import pandas as pd
import numpy as np
import streamlit as st  # 🎈 data web app development
import time  
import plotly.express as px  # interactive charts
from PIL import Image

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
"pancakeswap-token",
"chainlink",
"filecoin",
"arweave",
"immutable-x",
"metis-token",
"maker",
"loopring",
"dydx",
"the-graph",
"helium",
"euler",
"balancer",
"nexus-mutual",
"ethereum-name-service"
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
"DeFi",
"Oráculo",
"Armazenamento",
"Armazenamento",
"Layer 2",
"Layer 2",
"DeFi",
"Layer 2",
"Layer 2",
"Infraestrutura",
"Infraestrutura",
"DeFi",
"DeFi",
"Outros",
"Outros"
]
var1 = []
var2 = []
var3 = []
var4 =[]
var5 = []
im = Image.open('favicon.ico')

def is_what_percent_of(num_a, num_b):
    return ((num_a - num_b) / num_b) * 100

    
st.set_page_config(
    page_title="Titanium Crypto Overview",
    page_icon=im,
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
            p_1 = tree.xpath('//*[@id="general"]/div[1]/div[1]/div[3]/div[2]/div[2]/span/text()')[0]
            var1.append(p_7)
            var2.append(p_30)
            var3.append(c)
            var5.append(p_1)

        serie_1 = pd.Series(var1)
        serie_2 = pd.Series(var2)
        serie_3 = pd.Series(var3)
        serie_4 = np.array(categorias)
        serie_5 = pd.Series(var5)

        frame = {'Moeda':serie_3,'1d':serie_5,'7d': serie_1,'30d': serie_2,'Categoria':serie_4}

        result = pd.DataFrame(frame)
        result['7d'] = result['7d'].str.rstrip('%').astype('float') / 100.0
        result['30d'] = result['30d'].str.rstrip('%').astype('float') / 100.0
        result['1d'] = result['1d'].str.rstrip('%').astype('float') / 100.0
        result['Moeda_i'] = result['Moeda']
        result.set_index('Moeda_i', inplace=True)
        return result
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
destaque_pst_7d = f"{df.loc[df['7d'].idxmax(), 'Moeda']}"
destaque_ngt_7d = f"{df.loc[df['7d'].idxmin(), 'Moeda']}"
destaque_pst_30d = f"{df.loc[df['30d'].idxmax(), 'Moeda']}"
destaque_ngt_30d = f"{df.loc[df['30d'].idxmin(), 'Moeda']}"
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
            value= f"+{maior_semana}"
        )
    
        kpi2.metric(
            label=f"Destaque Negativo(7d): {destaque_ngt_7d}",
            value=menor_semana
        )
    
        kpi3.metric(
            label=f"Destaque Positivo(30d): {destaque_pst_30d}",
            value=f"+{maior_mes}"
        )

        kpi4.metric(
            label=f"Destaque Negativo(30d): {destaque_ngt_30d}",
            value=menor_mes
        )



escolha_cat,  = st.columns([1])

with escolha_cat:
    escolher_catego = st.selectbox(
        "Selecione o setor",
        ("Todos", "Pagamento", "DeFi", "Metaverso", "GameFi", "Layer 0", "Layer 1", "Layer 2","Oráculo","Armazenamento","Infraestrutura","Outros"),
    )
    if escolher_catego != "Todos":
        df = df[df["Categoria"] == escolher_catego]


    fig0 = px.bar(
    data_frame=df, y="1d", x="Moeda",
    )
    fig0.update_layout(yaxis_tickformat = '.2%', )
    fig0.update_traces(marker_color='rgb(223, 208, 134)')
    fig0.update_xaxes(tickangle=90)

    st.plotly_chart(fig0, use_container_width=True)
  
    
    
    
    fig1 = px.bar(
    data_frame=df, y="7d", x="Moeda",
    )
    fig1.update_layout(yaxis_tickformat = '.2%', )
    fig1.update_traces(marker_color='rgb(223, 208, 134)')
    fig1.update_xaxes(tickangle=90)
    st.plotly_chart(fig1, use_container_width=True)


    fig2 = px.bar(
    data_frame=df, x="Moeda", y="30d")
    fig2.update_layout(yaxis_tickformat = '.2%')
    fig1.update_traces(marker_color='rgb(223, 208, 134)')
    fig2.update_traces(marker_color='rgb(223, 208, 134)')
    fig2.update_xaxes(tickangle=90)
    st.plotly_chart(fig2, use_container_width=True)
    
    
   

    st.markdown("Cotação Cripto")
    filter_df = df.style.format({'7d':'{:.2%}','30d':'{:.2%}','1d':'{:.2%}'}).hide(axis='index')
    st.dataframe(filter_df)
    time.sleep(1)
