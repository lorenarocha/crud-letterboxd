import streamlit as st
import controllers.diary_controller as diary_controller
import models.diary as diary
import pandas as pd
from datetime import datetime 

st.title('Letterboxd')

st.sidebar.title('Menu')
st.sidebar.selectbox('Movie', ['Create', 'Read', 'Update', 'Delete'])

with st.form(key='include_movie'):
    input_name = st.text_input(label='Insira o nome do filme:')
    input_rating = st.slider(label='Escolha sua nota:', 
                                   min_value=0.0,
                                   max_value=5.0,
                                   step=0.5)
    input_watched_date = st.date_input(label='Qual data você assistiu esse filme?')
    input_rewatch = st.radio(label='Primeira vez assistindo?',
                                 options=['Sim', 'Não'])
    button_submit = st.form_submit_button('Enviar')
    
if button_submit:
        
    diary_controller.incluir(diary.Diary(input_name,
                                         input_rating,
                                         input_watched_date,
                                         input_rewatch))
    
    st.success('Filme incluído com sucesso')
    
    
diarylist = []

for row in diary_controller.read():
    diarylist.append([row.name,
                      str(row.rating),
                      row.watched_date,
                      row.rewatch])
    
df = pd.DataFrame(
    diarylist,
    columns=['Nome', 
             'Nota', 
             'Data em que foi assistido',
             'Reassistido']
)

st.experimental_show(df)
    
    
    
    


