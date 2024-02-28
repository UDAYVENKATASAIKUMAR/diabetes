import streamlit as st
from PIL import Image
import sys

def diabeticpredict():
    img=Image.open("images/team.jpg")

    with st.container():
        st.header("> Our site uses Machine Learning Algorithm such as RANDOM FOREST <")
        st.write("> It is a website that is designed to check whether the person is Diabetic or Not. ")
        st.write("> We are passionate about finding ways to make modren technologies to be more efficient and reliable.")
        st.write("> We are passionately working on this website to give users better accurate results.")
    with st.container():
        st.write("---")
        lcolumn,rcolumn=st.columns((3,2))
        with lcolumn:
            st.header("Team Working on this Project:")
            st.subheader("- Sk.AFSANA")
            st.subheader("- A.PAVANI")
            st.subheader("- E.NANI")
            st.subheader("- U.UDAY")
        with rcolumn:
            st.image(img)
        st.write("---")
        if st.button("Logout"):
            st.session_state.clear()
            st.markdown("<h1>Logging Out...</h1>", unsafe_allow_html=True)
            st.markdown("<h2>Also please close previous login tab...<h2>", unsafe_allow_html=True)
            st.markdown("<meta http-equiv='refresh' content='3; URL=http://localhost:8501/'>", unsafe_allow_html=True)
            sys.exit()
        




