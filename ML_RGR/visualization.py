import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st


data = pd.read_csv("csgo_task.csv")


class VisualizationCommand:
    def __init__(self, data):
        self.data = self.data

    def HeatMap(self):
        df_num = self.data.select_dtypes(include=np.number)
        df_corr = df_num.corr()
        plt.figure(figsize=(16, 6))
        sns.heatmap(df_corr, annot=True)
        st.pyplot(plt)

    def BoxPlot(self):
        df_num = self.data.select_dtypes(include=np.number)
        plt.figure(figsize=(16, 8))
        for i, column in enumerate(df_num.columns):
            plt.subplot(3, 8, i + 1)
            sns.boxplot(data=df_num, y=column)
            plt.title(column)

        plt.tight_layout()
        st.pyplot(plt)

    def BarChart(self):
        columns = ["ct_money", "t_money"]
        for col in columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(df[col], bins=100, kde=True)
            plt.title(f"Гистограмма для {col}")
            st.pyplot(plt)

    def PieСhart(self):
        fig1, ax1 = plt.subplots()
        ax1.pie(data["bomb_planted"].value_counts(), labels=data["bomb_planted"].values)
        plt.show()
