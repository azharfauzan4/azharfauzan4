import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! .")
st.image("IMG_20250501_103018.jpg", width=200)

st.title("XF")
st.header("XF")
angka = st.number_input("13:", value=0, step=1)

if (angka % 2) ==0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
