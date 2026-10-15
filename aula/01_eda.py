import pandas as pd
import plotly.express as px

df = pd.read_csv('data/coffes_sales.csv')
df.head(10)

#covert data
df ['data'] = pd.to_datetime (df ['data'])
df.head
#date in order
df = df.sort_values('data')
df.head()

df.isna() .sum()

df['media_7_dias'] = df ['vendas'].rolling(7).mean()
df.head()

fig = px.line(df,
    x='data',
    y=['vendas', 'media_7_dias'],
    title='vendas diárias da cafeteria'
)

fig.update_layout(
    xaxis_title='Data',
    yaxis_title='Unidades vendidas'
)
fig.show()

