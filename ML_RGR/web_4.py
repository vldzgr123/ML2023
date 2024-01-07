import streamlit as st
from Functions.selectModelFunc import *
import pandas as pd

uploaded_file = st.file_uploader("Выберите файл датасет", type="csv")

if uploaded_file is not None:
    
    data = pd.read_csv(uploaded_file)

    st.title("Предсказание поставлена ли бомба")

    type_model_select = st.selectbox(
        "Выберите тип модели",
        ["Обучение с учителем", "Обучение без учителя", "Ансабль", "Нейронная сеть"],
    )

    if type_model_select is not None:
        selected_model = ModelTypeSelector(type_model_select)

    data = FeaturesSelect()

    button_start = st.button("Предсказать")

    if button_start:
        ModelPrediction(selected_model, data)
