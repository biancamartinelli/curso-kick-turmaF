import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('anima_data.csv')

#titulo
st.title('Analise de dados sobre animais')

#subtitulo
st.subheader('Dados animais')
st.dataframe(df)

st.subheader('estatisticas simples')
#paragrafo simples
st.write(f'média da população geral: {df["População"].mean():.2f}')

#caixa de seleção
area_ocorrencia = st.selectbox('Selecione uma área',
    df['AreaOcorrencia'].unique()
                               )
dataframe_filtrado = df[df['AreaOcorrencia']== area_ocorrencia]
st.dataframe(dataframe_filtrado)

#grafico
plt.figure(figsize=(10, 6))
plt.bar(df['Nome'], df['Populacao'])
plt.xlabel('Nome do Animal')
plt.ylabel('População')
plt.title('População dos Animais')
plt.xticks(rotation=45)

#exibindo o grafico
st.pyplot(plt)

st.markdown('[Visite a página na Wikipedia](https://www.wikiwand.com/pt/Animalia)')