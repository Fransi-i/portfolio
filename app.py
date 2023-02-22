import streamlit as st
import pandas

df = pandas.read_csv("files/data.csv", sep=";")

def fill_columns(col, df, nr):
    with col:
        for index, row in df.iterrows():
            if index % 2 == nr :
                st.header(row["title"] )
                st.write(row["description"])
                st.image("images/" + row["image"])
                st.write(f"[source code]({row['url']})")

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.JPG", width=400)

with col2:
    st.title("Frans Isphording")
    content = """Hoi, Ik ben Frans Isphording, een al lang in de it werkzame ontwikkelaar met een brede interesse.
    Voorlopig probeer ik wat python te leren en wat web-toepassingen te maken om deze te oefenen.
    In het dagelijks (werkzame) leven ben ik werkzaam als Opentext AppWorks ontwikkelaar bij vele verschillende bedrijven"""
    st.info(content)

st.write("Hieronder wat apps waar ik mee bezig ben (alles in python) moet wat langer zijn om het goed te bekijken")

col3, col4, col5 = st.columns([1.5, 0.5, 1.5])  # een list met de relatieve kolombreedte
                                                # de middelste is leeg om de buitenste 2 te scheiden

fill_columns(col3, df, 0)
fill_columns(col5, df, 1)

