import streamlit as st
import pickle
import pandas as pd
import keras


def Teacher():
    st.title("Модель обучения")
    models = ["KNN", "Logistic Regression", "SVM"]

    return st.selectbox("Выберите модель", models)


def WithoutTeacher():
    st.title("Модель обучения")
    models = ["KMeans", "DBSCAN"]

    return st.selectbox("Выберите модель", models)


def Ancemble():
    st.title("Модель обучения")
    models = ["Bagging", "Gradient Boosting", "Stacking"]

    return st.selectbox("Выберите модель", models)


def NN():
    return "NN"


def ModelTypeSelector(model_type):
    match model_type:
        case "Обучение с учителем":
            return Teacher()
        case "Обучение без учителя":
            return WithoutTeacher()
        case "Ансабль":
            return Ancemble()
        case "Нейронная сеть":
            return NN()

def FeaturesSelect():
    st.write("time_left - длительность раунда")

    time_left = st.number_input("time_left:", value=175.0)

    st.write("ct_score - количество очков у команды контр-террористов")

    ct_score = st.number_input("ct_score:", value=0)

    st.write("t_score - количество очков у террористов")

    t_score = st.number_input("t_score:", value=0)

    st.write(
        "ct_health и t_health - суммарное здоровье контр-террористов и террористов соответственно"
    )

    ct_health = st.number_input("ct_health:", value=500)
    t_health = st.number_input("t_health:", value=500)

    st.write(
        "ct_armor и t_armor - суммарная броня контр-террористов и террористов соответственно"
    )

    ct_armor = st.number_input("ct_armor:", value=0)
    t_armor = st.number_input("t_armor:", value=0)

    st.write(
        "ct_money и t_money - суммарное количество денег контр-террористов и террористов соответственно"
    )

    ct_money = st.number_input("ct_money:", value=4000)
    t_money = st.number_input("t_money:", value=4000)

    st.write(
        "ct_helmets и t_helmets - суммарное количество шлемов контр-террористов и террористов соответственно"
    )

    ct_helmets = st.number_input("ct_helmets:", value=0)
    t_helmets = st.number_input("t_helmets:", value=0)

    st.write(
        "ct_defuse_kits - количество наборов обезвреживания бомбы у контр-террористов"
    )

    ct_defuse_kits = st.number_input("ct_defuse_kits:", value=0)

    st.write(
        "ct_players_alive и t_players_alive - количество живых контр-террористов и террористов соответственно"
    )

    ct_players_alive = st.number_input("ct_players_alive:", value=5)
    t_players_alive = st.number_input("t_players_alive:", value=5)

    data = pd.DataFrame(
        {
            "time_left": [time_left],
            "ct_score": [ct_score],
            "t_score": [t_score],
            "ct_health": [ct_health],
            "t_health": [t_health],
            "ct_armor": [ct_armor],
            "t_armor": [t_armor],
            "ct_money": [ct_money],
            "t_money": [t_money],
            "ct_helmets": [ct_helmets],
            "t_helmets": [t_helmets],
            "ct_defuse_kits": [ct_defuse_kits],
            "ct_players_alive": [ct_players_alive],
            "t_players_alive": [t_players_alive],
        }
    )

    st.write(data)

    return data


def ModelPrediction(model, data):
    st.write("Предсказанное значение:")

    match model:
        case "k-NN":
            with open("ML_RGR\Models\KNN.pickle", "rb") as file:
                knn = pickle.load(file)
            knn_pred = knn.predict(data)[0]
            st.write(knn_pred)
        case "Logistic Regression":
            with open("ML_RGR\Models\LG.pickle", "rb") as file:
                lg = pickle.load(file)
            lg_pred = lg.predict(data)[0]
            st.write(lg_pred)
        case "SVM":
            with open("ML_RGR\Models\SVM.pickle", "rb") as file:
                svc = pickle.load(file)
            svc_pred = svc.predict(data)[0]
            st.write(svc_pred)
        case "KNN":
            with open("ML_RGR\Models\KNN.pickle", "rb") as file:
                svc = pickle.load(file)
            svc_pred = svc.predict(data)[0]
            st.write(svc_pred)
        case "KMeans":
            with open("ML_RGR\Models\KMEANS.pickle", "rb") as file:
                svc = pickle.load(file)
            svc_pred = svc.predict(data)[0]
            st.write(svc_pred)
        case "DBSCAN":
            with open("ML_RGR\Models\DBSCAN.pickle", "rb") as file:
                svc = pickle.load(file)
            svc_pred = svc.labels_
            st.write(svc_pred)
        case "NN":
            model_loaded = keras.models.load_model("ML_RGR/Models/NN.h5")
            svc_pred = model_loaded.predict(data)[0][0]
            st.write(svc_pred)
