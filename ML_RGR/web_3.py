from visualization import *
import streamlit as st
import pandas as pd

vis = VisualizationCommand(pd.read_csv("ML_RGR\csgo_task.csv"))

st.title("Визуализация модели")

selected_value = st.selectbox(
    "Выберите вид визуализации",
    ["Тепловая карта", "Ящик с усами", "Гистограмма", "Круговая диаграмма"],
)

switch = {
    "Тепловая карта": vis.HeatMap(),
    "Ящик с усами": vis.BoxPlot(),
    "Гистограмма": vis.BarChart(),
    "Круговая диаграмма": vis.PieСhart(),
}
