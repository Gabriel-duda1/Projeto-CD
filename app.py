import streamlit as st
from ds.plot import plot_price

st.title('Histórico de Cotações')
st.write('Veja o histórico das cotações das empresas.')

ticker = st.sidebar.text_input(
    'Escolha o ticker:',
    value = 'AAPL'
)
fig = plot_price(ticker)
st.plotly_chart(fig)


draft.py


from functions.white_noise import white_noise
import plotly.express as px

time, values = white_noise(seed = 100)

px.line(
    x = time,
    y = values
 )