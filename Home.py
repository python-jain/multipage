import streamlit as st
import json
import streamlit_lottie as streamlit_lottie

st.set_page_config(
    page_title="MY FRIENDS",
    page_icon="✨",
)

st.title("STUPIDITY✨")
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
    
    lottie_coding = load_lottiefile("multipage/coding.json.json")
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        renderer="svg",
        height=None,
        width=None,
        key=None,
    )

st.subheader("A Website For My Friends")
st.sidebar.success("Select a page above.")
