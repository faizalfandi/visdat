import streamlit as st
import pandas as pd
import numpy as np

st.title("Bar Chart")
st.subheader("Praktikum-2 Visualisasi Data")
st.write("kelompok-3")
st.markdown("""
Nama Lengkap Anggota:
1. Faizal Fandi Mulyadi - 011022084
2. Faqih Al Fauzan - 0110222152
3. AFNAN AINUL MARDHIYYAH - 0110222128
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.bar_chart(df)