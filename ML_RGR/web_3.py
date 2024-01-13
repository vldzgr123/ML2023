from Functions.visualization import *
import streamlit as st
import pandas as pd


vis = VisualizationCommand(
    pd.read_csv("ML_RGR/csgo_task.csv").drop("Unnamed: 0", axis=1)
)

st.title("Визуализация набора данных")


st.header("Тепловая карта")
vis.HeatMap()

st.header("Ящик с усами")
vis.BoxPlot()

st.header("Гистограмма")
vis.BarChart()

st.header("Круговая диаграмма")
vis.PieСhart()
