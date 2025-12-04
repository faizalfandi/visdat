# import library yang dibutuhkan
import streamlit as st

# text element
# header - untuk membuat tulisan header
st.header("ini header") # untuk membuat folder
st.subheader("ini sub header") # untuk membuat subjudul yang lebih kecil
st.text("ini text biasa tanpa format") # untuk membuat teks polos tanpa format
st.markdown("**ini text bold** dan *ini text italic*") # markdown untuk memformat teks tebal/miring
st.caption("ini caption")
st.title("ini Judul")
st.markdown("""
- ini baris 1 
- ini menggunakan markdown multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini menggunakan markdown multibaris  

""")

#bagian 1
st.title("Praktikum 1 visualisasi data")
st.subheader("bagian 1-text-elements")
st.markdown("""
nama lengkap anggota:
1. Faizal Fandi Mulyadi - 011022084
2. Faqih Al Fauzan - 0110222152
3. AFNAN AINUL MARDHIYYAH - 0110222128
""")

#bagian 2
st.header("Displaying Latex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') # rumus trigonometri
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab''') # rumus kuadrat binominal

#bagian 3
st.header("Displaying Code")
st.subheader("Python Code")

# simpan ke variable
code = '''
def hello():
    print("hello, Streamlit!)
'''

#st.code() untuk menampilkan potongan kode dengan format rapi dan syntax highlighting
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
public class GFG {
        public static void main(String arg){
            System.out.printIn(Hello World);
        }
        
    }
""", language='java')
# fungsi st.code() bisa digunakan untuk bahasa pemrograman lain seperti Java, JavaScript, C++, HTML, dll

st.subheader("JavaScript Code")
st.code("""
<script>
try {
    addalert("Welcome guest); // kesalahan ketik (addalaert)
    sengaja dibuat untuk menampilkan error
}
catch(err) {
        document.getElementById("demo").innerHTML = err.message; //
        menampilkan pesan error di elemen HTML dengan id 'demo'
}
</script>
""", language='javascript')
#kode ini menunjukan contoh bagaiana menangani error (exception) di javascript.
#hasilnya tidak dijalankan di streamlit, tapi