import streamlit as st
from data_filter import df, df_invest_mensal, total_invest, total_retorno
from graficos import grafico_mensal, retorno_mensal
st.set_page_config(layout='wide', page_title='test')

st.metric('Banca inicial (Fev - 2023)', 'R$1.500,00')
tab1, tab2, tab3 = st.tabs(["Total de apostas", "Retorno mensal", "Acumulo da banca"])

#colocar o total de apostas ao longo do ano
with tab1:
    col1, col2 = st.columns(2)
    # st.dataframe(df)
    with col1:
        st.metric('Total de apostas', f'R$ {total_invest}','R$')
        st.plotly_chart(grafico_mensal, use_container_width=True)
    with col2:
        col3, col4 = st.columns(2)
        with col3:
            st.metric('Total de retorno das apostas', f'R$ {total_retorno}','R$')
        with col4:
            total = 831.42*100/1500
            st.metric('Total sobre a banca inicial', f'{total}%')
        st.plotly_chart(retorno_mensal, use_container_width=True)
        st.bar_chart(df, x='Quantidade apostas', y='Invest', color='Quantidade apostas')



#retorno mensal e autalização da banca trimestral (inicial R$1500)
with tab2:
    st.dataframe(df)

with tab3:
    st.write("Banca final")