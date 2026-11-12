# %%

import pandas as pd
from data_profiling import ProfileReport

df = pd.read_csv ("../data/coffes_sales.csv")

df ['data'] = pd.to_datetime(df['data'])
df = df.sort_values("data")

relatorio = ProfileReport(

    df,
    title="EDA - Vendas da cafeteria",
    tsmode=True,
    sortby='data',

)

relatorio.to_file("../Documentos")