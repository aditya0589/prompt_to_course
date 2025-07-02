import streamlit as st

def display_learning_plan(response_text: str):
    st.markdown("### Personalized Learning Plan")
    st.markdown(response_text)

    with st.expander("View Raw Text"):
        st.code(response_text)
