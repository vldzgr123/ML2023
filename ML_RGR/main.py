import streamlit as st
from st_pages import Page, show_pages

show_pages(
    [
        Page("web_1.py", "Об авторе"),
        Page("web_2.py", "О датасете"),
        Page("web_3.py", "Визуализация"),
        Page("web_4.py", "Предсказание модели"),
    ]
)

st.title('Расчетно-графическая работа по дисциплине "Машинное обучение"')
