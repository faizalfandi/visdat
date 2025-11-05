import streamlit as st
import pandas as pd     #untuk mengelola data dalam bentuk tabel
import numpy as np      # untuk membuat data numerik acak
import altair as alt    # untuk chart interaktif

st.title("PRAKTIKUM 1 VISUALISASI DATA")
st.subheader("Bagian 1. : Data Element")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan cewe = 0110222
""")

# Data Frame buat nampilin bentuk tabel baris kolom
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

#menampilkan data frame
st.dataframe(df)

#highlight nilai
st.subheader("Highlight Minimum Value di DataFrame")
#nilai terkecil di setiap kolom dataframe 
st.dataframe(df.style.highlight_min(axis=0))

#Tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
     np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

st.table(df)

st.subheader("📊 Metrics")

st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

col1, col2, col3 = st.columns(3)

col1.metric("Curah Hujan", "100 cm", "10 cm")
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse")
col3.metric(label="Pelanggan", value="100", delta="1", delta_color="off")

# Tambahan metric di bawah
st.metric(label="Speed", value="80 Mbps", delta="0")
st.metric("Trees", value="91,465", delta="11,000")

# Math calculations with no functions defined
"Adding 5 & 4 =", 5+4
# Displaying Variable 'a' and its value
a = 5
'a', a

# Markdown with Magic
"""
---
# Magic Feature
Markdown working without defining its function explicitly.
---
"""
# Dataframe using magic
import pandas as pd
df = pd.DataFrame({'col': [1,2]})
'dataframe', df
# Magic working on Charts
import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart


