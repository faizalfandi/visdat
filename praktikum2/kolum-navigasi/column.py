import streamlit as st

st.title("Columns")
st.subheader("Praktikum-2 Visualisasi Data")
st.write("kelompok-3")
st.markdown("""
Nama Lengkap Anggota:
1. Faizal Fandi Mulyadi - 011022084
2. Faqih Al Fauzan - 0110222152
3. AFNAN AINUL MARDHIYYAH - 0110222128
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah menteri ESDM pak Bahlil")
col1.image("https://tse2.mm.bing.net/th/id/OIP.KI4hC7mOgR1xKxKFAQZVnwHaEh?pid=Api&P=0&h=180")
col1.write("foto ini menginspirasi saya untuk bekerja keras")
col1.image("../../praktikum1/ganteng.jpeg")

