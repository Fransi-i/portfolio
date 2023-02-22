import streamlit as st

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