import pandas as pd
from tabulate import tabulate
import tabula

#---------Leitura do arquivo---------
pdf = tabula.read_pdf('../Data/16-02 a 19-02-23.pdf', pages='all')

#---------To dataframe------------
df = pd.DataFrame(pdf[0]) #Somente minha primeira tabela (apostas)
tabBets = pd.concat(pdf[1:], ignore_index=True) #concateno as outras tabela (para o futuro)

#---------Renomeação, separação de coluna e remoção--------------
df.columns=["Data","Quantidade apostas", "Valor investido", "Resultado banca"]
df[['Invest', 'Retorno']] = df["Valor investido"].str.split(' / ', expand=True) #separo minha coluna
df.drop(columns=['Valor investido'], inplace=True) #Removo a coluna que eu separei anteriormente.
df = df[df['Quantidade apostas'] != 'Sem apostas']
df.drop(df.index[-1], inplace=True) #essa linha deve ser movida para a leitura. na leitura de multiplos

#--------Transformação dos Dtypes--------------
try:
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
    df['Invest'] = df['Invest'].str.replace('R$ ', '').str.replace('[^\d.-]', '.').str.replace(',', '.').str.replace(' ', '').astype(float)
    df['Retorno'] = df['Retorno'].str.replace('R$ ', '').str.replace('[^\d.-]', '.').str.replace(',', '.').str.replace(' ', '').astype(float)
    df['Quantidade apostas'] = df['Quantidade apostas'].astype(int)
    df['Resultado banca'] = df['Resultado banca'].str.replace('%', '').str.replace('[^\d.-]', '.').str.replace(',', '.').str.replace(' ', '').astype(float)
except ValueError as errorCod:
    print("Unable to convert a value: ", errorCod)