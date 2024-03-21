import streamlit as st
from data_filter import df, df_invest_mensal, total_invest, total_retorno
from graficos import invest_mensal, retorno_mensal

st.set_page_config(layout='wide', page_title='test')
st.metric('Banca inicial (Fev - 2023 até Fev - 2024)', 'R$1.000,00')
tab1, tab2, tab3, renda_fixa = st.tabs(["Total de apostas", "Retorno mensal", "Acumulo da banca", "Renda fixa 3%"])

#colocar o total de apostas ao longo do ano
with tab1:
    col1, col2 = st.columns(2)
    # st.dataframe(df)

    with col1:
        st.metric('Total de apostas', f'R${total_invest:.2f}')
        st.plotly_chart(invest_mensal, use_container_width=True)

    with col2:
        col3, col4 = st.columns(2)

        with col3:
            st.metric('Total de retorno das apostas', f'R${total_retorno:.2f}','R$')
            st.metric('Retorno para o cliente', f'R${total_retorno*0.5:.2f}','R$')
        with col4:
            #chumbado o total, modificar para calcular sobre a variavel da banca e retorno das apostas.
            st.metric('Total sobre a banca inicial', f'{total_retorno*100/1000:.2f}%','R$')
            st.metric('Total retorno ao cliente (50%)''', f'{total_retorno*100/1000/2:.2f}%','R$')
        st.plotly_chart(retorno_mensal, use_container_width=True)
        st.bar_chart(df, x='Quantidade apostas', y='Invest', color='Quantidade apostas')

#retorno mensal e autalização da banca trimestral (inicial R$1500)
with tab2:
    st.dataframe(df)

with tab3:
    st.write("Banca final")

with renda_fixa:
    st.write("colocar banca da renda fixa e simulação da banca ao longo de X meses")