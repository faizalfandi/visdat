import streamlit as st
st.header("Ini header")
st.subheader("ieu sub header")
st.text("ieu text biasa")
st.markdown("**ini text bold** dan *ini text italic*")
st.markdown("""
- baris 1
1. baris 2
2. ini menggunakan markdown multibaris
* baris 3
* ini menggunakan markdown multi baris
""")
st.caption("ini caption")
st.title("ini judul")

import streamlit as st
st.title("PRAKTIKUM 1 VISUALISASI DATA")
st.subheader("Bagian 1. : Text Element")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan cewe = 0110222""")


#Bagian 2: Menampilkan rumus
st.header("Displaying Latex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''')
st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''')

#Bagian 3
st.header("Displaying Code")
st.subheader("Pythone Code")

#Simpan ke Variable
code = '''
def hello():
    Print("Hello, Streamlit)
'''

#st.code() untuk menampilkan potongan kode dengan format rapih
st.code(code, language='python')

st.subheader("Java Code")
st.code("""
Public class GFG {
        public static void main(string arg[]) {
            system.out.printIn("Hello World!);
        }
    }
""", language='java')
# Fungsi st.code bisa buat bahasa pemrograman lain kaya java, javascript, html dll

st.subheader("JavaScript Code")
st.code("""
<p id="demo"></p>
<script>
try {
    addalert("Welcome Guest!); // kesalahan ketik (addalert)
    sengaja dibuat untuk menimbulkan eror
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message; //
    menampilkan pesan eror di elemen HTML dengan id 'demi'
}
<script>
""", language='javaScript')