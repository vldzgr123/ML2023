import streamlit as st
from PIL import Image


st.title("Информация об авторе")

st.write('Загребельный Владислав Александрович, ФИТ-221.')
st.write(
    "Тема: «Разработка Web-приложения (дашборда) для инференса (вывода) моделей ML и анализа данных»"
)


st.image(
    Image.open("ML_RGR/Pictures/web_1_pictures/photo_2023-07-30_15-17-12.jpg"),
    width=450,
)
