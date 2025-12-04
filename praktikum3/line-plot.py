import streamlit as st
import matplotlib.pyplot as plt

# buat data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,65,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

# layout streamlit
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot",
                                                         "Multiple And Customization",
                                                         "Jenis Garis Untuk Menujukan Tren",
                                                         "Subplot"))

# Identitas kelompok
st.subheader("Kelompok 3")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Marddhiyyah = 0110222128
""")

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A")
    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Penjualan")
    st.pyplot(fig)


# Multiple Line Plot & customize
def customize_line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label="Product A", color='blue', linestyle='--', marker='o')
    ax.plot(months, product_B_sales, label="Product B", color='red', linestyle='-', marker='x')
    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Penjualan")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Data sample tambahan
product_C_sales = [18,22,25,28,32,38,43,47,50,55,60,78]
product_D_sales = [5,9,11,14,17,23,26,29,30,35,37,40]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_C_sales, label="Product C", color='blue', linestyle='-.')
    axs.plot(months, product_D_sales, label="Product D", color='red', linestyle=';')
    axs.set_title('Penjualan Produk A per Bulan')
    axs.set_xlabel("Bulan")
    axs.set_ylabel("Penjualan")
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)

# subplot
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# plot pertama untuk product C
    axs[0].plot(months, product_C_sales, label='Product C', color='green', marker='d')
    axs[0].set_title('Penjualan Product C per bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid('True')

# plot pertama untuk product D
    axs[1].plot(months, product_D_sales, label='Product D', color='purple', marker='s')
    axs[1].set_title('Penjualan Product C per bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid('True')

    plt.tight_layout()
    st.pyplot(fig)

# logika untuk menampilkan visualisasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple And Customization":
    customize_line_plot()
elif option == "Jenis Garis Untuk Menujukan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()