#from tkinter import Image
from lxml import html
import requests
import pandas as pd
import numpy as np
import streamlit as st  # 🎈 data web app development
import time  
import plotly.express as px  # interactive charts
from PIL import Image

apelidos = [
"Ripple(XRP)", 
"Cosmos(ATOM)", 
"Algorand(ALGO)", 
"Celo(CELO)", 
"Sandbox(SAND)", 
"Kava(KAVA)", 
"Stellar(XLM)", 
"Compound(COMP)", 
"Nexo(NEXO)", 
"Polygon(MATIC)", 
"Theta (THETA)", 
"Havven (HAV)", 
"Uniswap (UNI)", 
"Curve (CRV)", 
"Polkadot (DOT)", 
"Solana (SOL)", 
"Optimism (OP)", 
"Bitcoin (BTC)", 
"Lido Finance (LDO)", 
"GMX (GMX)", 
"Chilliz (CHZ)", 
"Tron (TRN)", 
"Ethereum (ETH)", 
"Near Protocol (NEAR)", 
"Enjin Coin (ENJ)", 
"Cardano (ADA)", 
"Shiba Inu (SHIB)", 
"Gala Games (GALA)", 
"Avalanche (AVAX)", 
"FTX Token (FTX", 
"Neo (NEO)", 
"Kusama (KSM)", 
"Ravencoin (RVN)", 
"Flow (FLOW)", 
"Pancake Swap (CAKE)", 
"Chainlink (LINK)", 
"Filecoin (FIL)", 
"Arweave (AR)", 
"Immutable-X (IMX)", 
"Metis-DAO (METIS)", 
"Maker DAO (MKR)", 
"Loopring (LPC)", 
"dYdX (DYDX)", 
"The Graph(GRT)", 
"Helium (HNT)", 
"Euler Finance (EUL)", 
"Balancer (BAL)", 
"Nexus Mutual (NXM)", 
"Ethereum Name Service (ENS)"    
]

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
var6 = []
var7 =[]
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
            ticker = tree.xpath('///*[@id="conversion-calculator"]/div[2]/div[1]/span/text()')[0]
            #price_usd = tree.xpath('/html/body/div[5]/div[5]/div[1]/div/div[1]/div[2]/div/text()')[0]
            var1.append(p_7)
            var2.append(p_30)
            var3.append(c)
            var5.append(p_1)
            var6.append(ticker)
            #var7.append(price_usd)
            
            


        serie_1 = pd.Series(var1)
        serie_2 = pd.Series(var2)
        serie_3 = pd.Series(var3)
        serie_4 = np.array(categorias)
        serie_5 = pd.Series(var5)
        serie_6 = pd.Series(var6)
        serie_7 = np.array(apelidos)

        frame = {'Symbol':serie_6,'Moeda':serie_3,'1d':serie_5,'7d': serie_1,'30d': serie_2,'Categoria':serie_4,'Teste':serie_7}

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
    st.image("logo.png", width=225)

st.title("Crypto Overview")


# top-level filters


# creating a single-element container
placeholder = st.empty()

# dataframe filter
destaque_pst_1d = f"{df.loc[df['1d'].idxmax(), 'Teste']}" 
destaque_ngt_1d = f"{df.loc[df['1d'].idxmin(), 'Teste']}" 
destaque_pst_7d = f"{df.loc[df['7d'].idxmax(), 'Teste']}"
destaque_ngt_7d = f"{df.loc[df['7d'].idxmin(), 'Teste']}"
destaque_pst_30d = f"{df.loc[df['30d'].idxmax(), 'Teste']}"
destaque_ngt_30d = f"{df.loc[df['30d'].idxmin(), 'Teste']}"
# near real-time / live feed simulation
for seconds in range(200):
    maior_dia = ('{:,.2%}'.format(df["1d"].max()))
    menor_dia = ('{:,.2%}'.format(df["1d"].min()))
    maior_semana = ('{:,.2%}'.format(df["7d"].max()))
    menor_semana = ('{:,.2%}'.format(df["7d"].min()))
    maior_mes =    ('{:,.2%}'.format(df["30d"].max()))
    menor_mes =    ('{:,.2%}'.format(df["30d"].min()))
    with placeholder.container():
        kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
        
        kpi1.metric(
            label=f"Destaque Positivo (1d):",
            value= destaque_pst_1d,
            delta = maior_dia
        )
    
        kpi2.metric(
            label=f"Destaque Negativo (1d):",
            value= destaque_ngt_1d,
            delta = menor_dia
        )
    
        kpi3.metric(
            label=f"Destaque Positivo (7d):",
            value= destaque_pst_7d,
            delta = maior_semana
        )

        kpi4.metric(
            label=f"Destaque Negativo (7d):",
            value=destaque_ngt_7d,
            delta = menor_semana
        )
        kpi5.metric(
            label=f"Destaque Positivo (30d):",
            value=destaque_pst_30d,
            delta=maior_mes
        )
        kpi6.metric(
            label=f"Destaque Negativo (30d):",
            value=destaque_ngt_30d,
            delta = menor_mes
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
    data_frame=df, y="1d", x="Symbol",
    )
    fig0.update_layout(yaxis_tickformat = '.2%', )
    fig0.update_traces(marker_color='rgb(223, 208, 134)')
    fig0.update_xaxes(tickangle=-60)

    st.plotly_chart(fig0, use_container_width=True)
  
    
    
    
    fig1 = px.bar(
    data_frame=df, y="7d", x="Symbol",
    )
    fig1.update_layout(yaxis_tickformat = '.2%', )
    fig1.update_traces(marker_color='rgb(223, 208, 134)')
    fig1.update_xaxes(tickangle=-60)
    #fig1.update_yaxes(visible=False, showticklabels=False)
    st.plotly_chart(fig1, use_container_width=True)


    fig2 = px.bar(
    data_frame=df, x="Symbol", y="30d")
    fig2.update_layout(yaxis_tickformat = '.2%')
    fig1.update_traces(marker_color='rgb(223, 208, 134)')
    fig2.update_traces(marker_color='rgb(223, 208, 134)')
    fig2.update_xaxes(tickangle=-60)
    st.plotly_chart(fig2, use_container_width=True)
    
    
   

    st.markdown("Cotação Cripto")
    filter_df = df.style.format({'7d':'{:.2%}','30d':'{:.2%}','1d':'{:.2%}'}).hide(axis='index')
    st.dataframe(filter_df)
    time.sleep(1)
    print(var7)
