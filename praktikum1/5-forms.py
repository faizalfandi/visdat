import streamlit as st
import datetime
import pandas as pd

st.title("PRAKTIKUM 1 VISUALISASI DATA")
st.subheader("Bagian 1. : Data Element")
st.markdown("""
**Nama Lengkap Anggota**
1. Faizal Fandi Mulyadi = 0110222184
2. Faqih Al Fauzan = 0110222152
3. Afnan Ainul Marddhiyyah = 0110222128
""")

st.title("Text Box")
# Creating Text box
name = st.text_input("Enter your Name")
st.write("Your Name is ", name)

# Creating Text Area
input_text = st.text_area("Enter your Review")
# Printing entered text
st.write("""You entered: \n""",input_text)

# Create number input
st.number_input("Enter your Number")

# Create number input
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

st.title("Time")
# Defining Time Function
st.time_input("Select Your Time")

st.title("Date")
# Defining Date Function
st.date_input("Select Date")
st.title("Date")
# Defining Time Function
st.date_input("Select Your Date", value=datetime.date(1989, 12, 25),
min_value=datetime.date(1987, 1, 1),
max_value=datetime.date(2005, 12, 1))

st.title("Select Color")
# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

# Dataset Upload
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV",type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,
                        "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

# Submit Button
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')
st.write(a)



import streamlit as st
import datetime
import pandas as pd

# ===============================
# HEADER SECTION
# ===============================
st.set_page_config(page_title="Data Visualization Practicum", layout="centered")

st.title("📊 PERBAIKI UI SUPAYA LEBIH ENAK DILIHAT")
st.subheader("Part 1: Data Elements")
st.markdown("""
**Team Members**
1. Faizal Fandi Mulyadi — 0110222184  
2. Faqih Al Fauzan — 0110222152  
3. Afnan Ainul Marddhiyyah — 0110222128
""")

st.markdown("---")

# ===============================
# TEXT INPUT SECTION
# ===============================
st.header("📝 Text Inputs")

name = st.text_input("Enter your name")
if name:
    st.success(f"Your name is: **{name}**")

input_text = st.text_area("Enter your review")
if input_text:
    st.info(f"You entered:\n\n{input_text}")

st.markdown("---")

# ===============================
# NUMBER INPUT SECTION
# ===============================
st.header("🔢 Number Inputs")

col1, col2 = st.columns(2)
with col1:
    st.number_input("Enter a simple number")
with col2:
    num = st.number_input("Enter a number (0–10)", 0, 10, 5, 2)
    st.caption("Min: 0 | Max: 10 | Default: 5 | Step: 2")

st.write("Total value after applying step value:", num)

st.markdown("---")

# ===============================
# TIME & DATE INPUT SECTION
# ===============================
st.header("⏰ Time & Date Inputs")

col1, col2 = st.columns(2)
with col1:
    selected_time = st.time_input("Select a time")
    st.write("Selected time:", selected_time)

with col2:
    selected_date = st.date_input("Select a date")
    st.write("Selected date:", selected_date)

st.date_input(
    "Select a date (with range)",
    value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1)
)

st.markdown("---")

# ===============================
# COLOR PICKER SECTION
# ===============================
st.header("🎨 Color Picker")
color_code = st.color_picker("Choose your color")
st.markdown(f"**Selected color code:** `{color_code}`")

st.markdown("---")

# ===============================
# DATASET UPLOAD SECTION
# ===============================
st.header("📂 CSV Data Upload")

data_file = st.file_uploader("Upload a CSV file", type=["csv"])
if data_file is not None:
    st.success("✅ File uploaded successfully!")
    with st.expander("View File Details"):
        file_details = {
            "File Name": data_file.name,
            "File Type": data_file.type,
            "File Size": f"{data_file.size:,} bytes"
        }
        st.json(file_details)

    df = pd.read_csv(data_file)
    st.subheader("📈 Preview of Uploaded Data:")
    st.dataframe(df)
else:
    st.info("No file uploaded yet. Please upload a CSV file.")

st.markdown("---")

# ===============================
# FORM SUBMISSION SECTION
# ===============================
st.header("📨 Submit Form")

with st.form(key="text_form"):
    text_input = st.text_input("Enter any text")
    submitted = st.form_submit_button("Submit")

if submitted:
    if text_input.strip() != "":
        st.success(f"You submitted: **{text_input}**")
    else:
        st.warning("Please enter some text before submitting.")

st.markdown("---")
st.caption("© 2025 Data Visualization Practicum — STT Terpadu Nurul Fikri")
