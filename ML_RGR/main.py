import streamlit as st

from st_pages import Page, Section, show_pages, add_page_title

# st.set_page_config(page_title = "New Name")

show_pages(
    [
        Page("ML_RGR\web_1.py", "Об авторе"),
        Page("ML_RGR\web_2.py", "О датасете"),
        Page("ML_RGR\web_3.py", "Визуализация"),
        Page("ML_RGR\web_4.py", "Предсказание модели"),
    ]
)

st.title("Расчетно-графическая работа")