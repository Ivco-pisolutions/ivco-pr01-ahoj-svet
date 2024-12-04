import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title("🤽‍♂️ XBS Amatéri")
st.write(
    "Toto je informačná stránka klubu XBS Amatéri"
)

data = pd.DataFrame({
        "Kategorie" : ["A", "B", "C", "D"],
        "Hodnoty" : [25, 40, 35, 30]
})

st.write("Tabulka s datami:")
st.dataframe (data)

fig = px.bar(data, x= "Kategorie", y="Hodnoty", title = "Stlpcovy graf v plotly")

st.plotly_chart(fig)

if st.button ("Informacne okno"):
    st.info("Toto je informacne okno")

if st.button ("Upozornovacie okno"):
    st.warning("Toto je upozornovacie okno")

if st.button ("Chybove okno"):
    st.error("Toto je chybove okno")

user_input = st.text_input("Ako sa volas: ")
st.write(f"Volas sa {user_input}")


edited_data = st.data_editor ( data, num_rows="dynamic")


st.write("👍 Upravena tabulka")
st.dataframe(edited_data)

st.write("😱 Stlpcovy graf: ")

fig_bar = px.bar(edited_data, x= "Kategorie", y="Hodnoty", title = " upraveny Stlpcovy graf v plotly")

st.plotly_chart(fig_bar)


st.write("😱 Koláčový graf: ")

fig_pie = px.pie(edited_data, names = "Kategorie", values="Hodnoty",
                 title="Upraveny kolacovy graf")

st.plotly_chart(fig_pie)