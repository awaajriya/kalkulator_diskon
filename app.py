%%writefile app.py
import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Kalkulator Diskon Pro", page_icon="🛒")

# CSS Kustom untuk tampilan Mobile yang cantik
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #2e7d32; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛒 Kasir Diskon")
st.write("Hitung belanjaanmu jadi lebih mudah!")

# Input Area
with st.container():
    nama_barang = st.text_input("Nama Barang", placeholder="Misal: Kemeja")
    harga = st.number_input("Harga Barang (Rp)", min_value=0, step=1000, value=0)
    diskon = st.slider("Diskon (%)", 0, 100, 10)

# Tombol Hitung
if st.button("Hitung Sekarang"):
    if harga > 0:
        potongan = harga * (diskon / 100)
        total = harga - potongan
        
        st.balloons() # Efek perayaan
        
        # Kartu Hasil
        st.markdown(f"""
        <div style="background-color: white; padding: 20px; border-radius: 15px; border-left: 10px solid #2e7d32; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h3 style="margin:0;">Total Bayar:</h3>
            <h1 style="color: #2e7d32; margin:0;">Rp {total:,.0f}</h1>
            <p style="color: grey;">Hemat: Rp {potongan:,.0f}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Masukkan harga barang terlebih dahulu!")
