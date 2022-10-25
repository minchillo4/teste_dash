from lxml import html
import requests
import pandas as pd
import numpy as np
import streamlit as st  # 🎈 data web app development
import time  
import plotly.express as px  # interactive charts
from PIL import Image

apelidos = [
"Aave",
"Ripple", 
"Cosmos", 
"Algorand", 
"Celo", 
"Sandbox", 
"Kava", 
"Stellar", 
"Compound", 
"Nexo", 
"Polygon", 
"Theta", 
"Decentraland", 
"Uniswap", 
"Curve", 
"Polkadot", 
"Solana", 
"Optimism", 
"Bitcoin", 
"Lido Finance", 
"GMX", 
"Chilliz", 
"Tron", 
"Ethereum", 
"Near Protocol", 
"Enjin", 
"Cardano", 
"Shiba Inu", 
"Gala Games", 
"Avalanche", 
"FTX Token", 
"Neo", 
"Kusama", 
"Ravencoin ", 
"Flow", 
"Pancake Swap", 
"Chainlink", 
"Filecoin", 
"Arweave", 
"Immutable-X", 
"Metis-DAO ", 
"Maker DAO", 
"Loopring", 
"dYdX", 
"The Graph", 
"Helium", 
"Euler Finance", 
"Balancer", 
"Nexus Mutual", 
"Ethereum Name Service"    
]

moedas = [
"aave",
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
"decentraland", 
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
"DeFi",
"Pagamento", 
"Layer 0", 
"Layer 1", 
"Layer 1", 
"GameFi/Metaverso", 
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
"GameFi/Metaverso", 
"Layer 1", 
"Layer 1", 
"Layer 1", 
"GameFi/Metaverso", 
"Layer 1", 
"Pagamento", 
"GameFi/Metaverso", 
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
var7 = []
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
            var1.append(p_7)
            var2.append(p_30)
            var3.append(c)
            var5.append(p_1)
            var6.append(ticker)
            
            
            


        serie_1 = pd.Series(var1)
        serie_2 = pd.Series(var2)
        serie_3 = pd.Series(var3)
        serie_4 = np.array(categorias)
        serie_5 = pd.Series(var5)
        serie_6 = pd.Series(var6)
        serie_7 = np.array(apelidos)

        frame = {'Symbol':serie_6,'Moeda':serie_3,'1d':serie_5,'7d': serie_1,'30d': serie_2,'Categoria':serie_4,'Nome':serie_7}

        result = pd.DataFrame(frame)
        result['7d'] = result['7d'].str.rstrip('%').astype('float') / 100.0
        result['30d'] = result['30d'].str.rstrip('%').astype('float') / 100.0
        result['1d'] = result['1d'].str.rstrip('%').astype('float') / 100.0
        result['Moeda_i'] = result['Moeda']
        result['Name&Symb'] = result['Nome'] + '(' + result['Symbol'] + ')'
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
destaque_pst_1d = f"{df.loc[df['1d'].idxmax(), 'Name&Symb']}" 
destaque_ngt_1d = f"{df.loc[df['1d'].idxmin(), 'Name&Symb']}" 
destaque_pst_7d = f"{df.loc[df['7d'].idxmax(), 'Name&Symb']}"
destaque_ngt_7d = f"{df.loc[df['7d'].idxmin(), 'Name&Symb']}"
destaque_pst_30d = f"{df.loc[df['30d'].idxmax(), 'Name&Symb']}"
destaque_ngt_30d = f"{df.loc[df['30d'].idxmin(), 'Name&Symb']}"
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

        st.markdown("""<style>[data-testid="stMetricValue"] {font-size: 25px;}</style>""",unsafe_allow_html=True,)
        
        kpi1.metric(
            label=f"Best Performance (1d):",
            value= destaque_pst_1d,
            delta = maior_dia
        )
    
        kpi2.metric(
            label=f"Worst Performance (1d):",
            value= destaque_ngt_1d,
            delta = menor_dia
        )
    
        kpi3.metric(
            label=f"Best Performance (7d):",
            value= destaque_pst_7d,
            delta = maior_semana
        )

        kpi4.metric(
            label=f"Worst Performance (7d):",
            value=destaque_ngt_7d,
            delta = menor_semana
        )
        kpi5.metric(
            label=f"Best Performance (30d):",
            value=destaque_pst_30d,
            delta=maior_mes
        )
        kpi6.metric(
            label=f"Worst Performance (30d):",
            value=destaque_ngt_30d,
            delta = menor_mes
        )



escolha_cat,  = st.columns([1])

with escolha_cat:
    escolher_catego = st.selectbox(
        "Choose a category",
        ("Todos", "Pagamento", "DeFi", "GameFi/Metaverso", "Layer 0", "Layer 1", "Layer 2","Oráculo","Armazenamento","Infraestrutura"),
    )
    if escolher_catego != "Todos":
        df = df[df["Categoria"] == escolher_catego]

    
    fig0 = px.bar(
    data_frame=df, y="1d", x="Symbol",title="Performance (1d)",height = 700, color="1d", range_color=[-0.02, 0.02], color_continuous_scale=['rgb(100,0,0)','rgb(6,41,0)'])
    fig0.update_layout(yaxis_tickformat = '.2%', xaxis_title=" ")
    fig0.update_traces(hovertemplate=  'Variação: %{y}<br>Moeda: %{x}')
    fig0.update_xaxes(tickangle=-60)

    st.plotly_chart(fig0, use_container_width=True)
  
    
    
    
    fig1 = px.bar(          
    data_frame=df, y="7d", x="Symbol",title="Performance (7d)", color='7d', range_color=[-0.05, 0.02], color_continuous_scale=['rgb(100,0,0)','rgb(6,41,0)']
    )
    fig1.update_layout(yaxis_tickformat = '.2%', xaxis_title=" ",height = 700)
    fig1.update_traces(hovertemplate='Variação: %{y}<br>Moeda: %{x}')
    fig1.update_xaxes(tickangle=-60)
    #fig1.update_yaxes(visible=False, showticklabels=False)
    st.plotly_chart(fig1, use_container_width=True)


    fig2 = px.bar(
    data_frame=df, x="Symbol", y="30d",title="Performance (30d)",height = 700,range_color=[-0.05, 0.02], color_continuous_scale=['rgb(100,0,0)','rgb(6,41,0)'],color="30d")
    fig2.update_layout(yaxis_tickformat = '.2%',xaxis_title=" ")
    fig2.update_traces(hovertemplate='Variação: %{y}<br>Moeda: %{x}')
    fig2.update_xaxes(tickangle=-60)
    st.plotly_chart(fig2, use_container_width=True)
    
    
   

    st.markdown("Overview Table")

    new_df = pd.DataFrame()
    new_df['Symbol'] = df['Symbol']
    new_df['Nome'] = df['Nome']
    new_df['Categoria'] = df['Categoria']
    new_df['1d'] = df['1d']
    new_df['7d'] = df['7d']
    new_df['30d'] = df['30d']
    
    
   
   

    blankIndex=['']*len(new_df)
    new_df.index=blankIndex
 
    
  
    st.dataframe(new_df.style.format({'7d':'{:.2%}','30d':'{:.2%}','1d':'{:.2%}'}))
    
    
