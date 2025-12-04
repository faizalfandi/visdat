import streamlit as st
import pandas as pd # untuk mengelola data dalam bentuk tabel (dataframe)
import numpy as np # untuk membuat data numerik acak
import altair as alt # untuk membuat chart interaktif

st.title("Praktikum 1 visualisasi data")
st.subheader("Bagian 2-data-elements")
st.markdown("""
nama lengkap anggota:
1. Faizal Fandi Mulyadi - 011022084
2. Faqih Al Fauzan - 0110222152
3. AFNAN AINUL MARDHIYYAH - 0110222128
""")
st.subheader("DATA FRAME")
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

#menampilkan dataframe
st.dataframe(df)

#highlight nilai minimum
st.subheader("Highlight Minimum Value di DataFrame")

#highlight nilai terkecil disetiap kolom dataframe
# axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

#tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)
#menampilkan tabel statis
st.table(df)

#metrics: komponen tampilan angka penting
st.subheader("Metrics")
#menampilkan metrik tunggal (nilai utama + perubahan nilai)
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

col1, col2, col3 = st.columns(3)

#menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") #naik dan baik
col2.metric(label="Populasi", value="123 miliar", delta="1 miliar", delta_color="inverse") #naik tapi buruk
col3.metric(label="Pelanggann", value=100, delta=10, delta_color="off") # netral (tidak baik, tidak buruk)

#menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) # kosong # naik baik karena di seting default
st.metric("Trees", value="91456", delta="-113649")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
)

#defining multiple arguments in write function
st.write('here is our data', df, 'data is in dataframe format.\n', "\nwrite is super function")

df = pd.DataFrame(
    np.random.randn(10,2),
    columns=['a', 'b']
)
#defininng chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b']
)
#defining chart in write() function
st.write(chart)

#math calculation with no fuction defined
"Adding 5 & 4 =", 5+4
#displaying variable 'a' and its value
a = 5
'a', a

#markdown with magic
"""
#magic feature
markdown working without defining its function explicitly.
"""
#datafrma using magic
import pandas as pd
df = pd.DataFrame({'col': [1,]})
'dataframe', df

#magic working on charts
import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
#magic chart
"chart", chart
