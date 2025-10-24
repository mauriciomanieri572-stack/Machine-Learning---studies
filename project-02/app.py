import streamlit as st  #IMPORTANTE ESTAR COM O VEN ATIVO!!!
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('pizzas.csv')

modelo = LinearRegression()
x = df[['diametro']] 
y = df['preco'] 

st.title('Prevendo um valor de uma pizza')
st.divider()

diametro = st.number_input("Informe o tamanho do diametero da pizza")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0]
    st.write(f'O valor da pizza com diâmetro de {diametro} é de R$ {preco_previsto}.')