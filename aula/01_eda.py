import pandas as pd
import plotly.express as px

df = pd.read_csv('../data/coffes_sales.csv')
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

#dias da semana
df['dia_semana'] = df ['data'].dt.day_of_week
df.head()

#média por dia
media_por_dia = df.groupby('dia_semana')['vendas'].mean()

media_por_dia.index = ['Seg','Ter','Qua', 'Qui', 'Sex', 'Sab', 'Dom']
fig = px.bar (

        x=media_por_dia.index,
        y=media_por_dia.values,
        title='Media de vendas por dia da semana'
)
fig.update_layout(
    xaxis_title="Dia da semana",
    yaxis_title="Média de unidades vendidas"
)
fig.show()

#boxplots
fig = px.box(
    df,
    x='dia_semana',
    y='vendas',
    points='outliers',
    title='Distribuição de vendas por dia da semana'
)
fig.update_xaxes(
    tickvals=['0','1','2', '3','4','5','6'],
    ticktext=['Seg','Ter','Qua', 'Qui', 'Sex', 'Sab', 'Dom']
    )

fig.update_layout(
    xaxis_title="Dia da semana",
    yaxis_title="Unidades de vendas"

    )
fig.show()