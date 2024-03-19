import plotly.express as px
from data_filter import df, df_invest_mensal, total_invest, df_retorno_mensal


grafico_mensal = px.line(df_invest_mensal,
                         x='Mes',
                         y='Invest',
                         markers=True,
                         range_y=(0,df_invest_mensal.max()),
                         color='Ano',
                         line_dash='Ano',
                         title='Total de apostas - R$'
                         )
retorno_mensal = px.line(df_retorno_mensal,
                         x='Mes',
                         y='Retorno',
                         markers=True,
                         range_y=(0,df_invest_mensal.max()),
                         color='Ano',
                         line_dash='Ano',
                         title='Retorno mensal - R$'
                         )