'''
Autor: Elmer M.Brum
Data: 03/2024
Description:Read all pdf's and do a PDF scraping, data separation, data filter, data convert. 
    to analyse all investments from JAinvestimento week report.

Version: 0.1
What next: After all the analysis of the bets is done,
            the filtering and separation of the data by games and sports types will be carried out
'''
import pandas as pd

df = pd.read_csv('./Data/ate_11-03-24.csv')
df['Data'] = pd.to_datetime(df['Data'])

pd.read_sql_table

#------------Investimento mensal------------
df_invest_mensal = df.set_index('Data').groupby(pd.Grouper(freq='M'))['Invest'].sum().reset_index()
df_invest_mensal['Ano'] = df_invest_mensal['Data'].dt.year
df_invest_mensal['Mes'] = df_invest_mensal['Data'].dt.month

#------------Valor / de apostas----------
total_invest = df['Invest'].sum()
# total_invest = '{:,.2f}'.format(total_invest)
total_retorno = df['Retorno'].sum()
# total_retorno = '{:,.2f}'.format(total_retorno)


#------------Retorno mensal--------------
df_retorno_mensal = df.set_index('Data').groupby(pd.Grouper(freq='M'))['Retorno'].sum().reset_index()
df_retorno_mensal['Ano'] = df_retorno_mensal['Data'].dt.year
df_retorno_mensal['Mes'] = df_retorno_mensal['Data'].dt.month
