import streamlit as st
from data_filter import df

st.set_page_config(layout='wide', page_title='test')
st.dataframe(df)
st.bar_chart(df, x='Quantidade apostas', y='Invest', color='Quantidade apostas')