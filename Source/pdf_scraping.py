# import pandas as pd
# import tabula
# import os

''''
Because take a long time to read and extract all tables (only bets) from a 50 pdf files, I exported all data filtered in to a CSV file.
'''

# path_pdf = "Analise-investimento\Data"
# tabelas = []
# for arquivo in os.listdir(path_pdf):
#     if arquivo.endswith('.pdf'):
#         # Extrair tabelas da primeira página do arquivo PDF
#         try:
#             df = tabula.read_pdf(os.path.join(path_pdf, arquivo), pages=1)[0] #cocateno a path e o nome do arquivo.
#             df.columns=["Data","Quantidade apostas", "Valor investido", "Resultado banca"]
#             df.drop(df.index[-1], inplace=True)
#             tabelas.append(df)
#         except Exception as e:
#             print(f"Erro ao processar o arquivo {arquivo}: {e}")

# #---------Concatenação das tabelas e renomeação----------
# df = pd.concat(tabelas, ignore_index=True)
# df.columns=["Data","Quantidade apostas", "Valor investido", "Resultado banca"]

# #---------Filtragem dos dados ------------
# df.dropna(how='any', axis=0, inplace=True)
# df[['Invest', 'Retorno']] = df["Valor investido"].str.split(r'\s*\/\s*', expand=True) #separo minha coluna
# df.drop(columns=['Valor investido'], inplace=True) #Removo a coluna que eu separei anteriormente.
# df = df[df['Quantidade apostas'] != 'Sem apostas']

# try:
#     df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
#     df['Invest'] = df['Invest'].str.replace(r'[^\d.-]', '', regex=True).astype(float)
#     df['Retorno'] = df['Retorno'].str.replace(r'[^\d.-]', '', regex=True).astype(float)
#     df['Resultado banca'] = df['Resultado banca'].str.replace(' ', '', regex=True).str.replace('--', '-', regex=True)
#     # Remover o '%' e todos os caracteres não numéricos, exceto o '.' para preservar o ponto decimal
#     df['Resultado banca'] = df['Resultado banca'].str.replace('%', '').str.replace(r'[^\d.-]', '', regex=True)
#     # Substituir múltiplos pontos decimais por apenas um
#     df['Resultado banca'] = df['Resultado banca'].str.replace(r'\.{2,}', '.', regex=True)
#     # Substituir a vírgula por ponto como separador decimal
#     df['Resultado banca'] = df['Resultado banca'].str.replace(',', '.')
#     # Converter para float
#     df['Resultado banca'] = df['Resultado banca'].astype(float)
#     df['Quantidade apostas'] = df['Quantidade apostas'].astype(int)
# except ValueError as errorCod:
#     print("Unable to convert a value: ", errorCod)

# #--------Adequação dos dados-----------
# #ao transformar para float e int o ponto foi movido (problema no regex?)
# df['Invest'] = df['Invest'] / 100
# df['Resultado banca'] = df['Resultado banca'] / 10000
# df['Retorno'] = df['Retorno'] / 100
# print(df)