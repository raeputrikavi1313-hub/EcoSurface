import streamlit as st
from data.parameter_data import sampling_data, baku_mutu

# =========================
# ⚙️ CONFIG UI
# =========================
st.set_page_config(
    page_title="EcoSurface",
    layout="wide",
    page_icon="🌊"
)

# =========================
# 🎨 GLOBAL CSS (UI MODERN)
# =========================
st.markdown("""
<style>
body {
    background-color: #FFFFFF;
}

.block-container {
    padding: 1.5rem 2rem;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    border-left: 6px solid #2E8B57;
}

.good {
    color: #2E8B57;
    font-weight: bold;
}

.bad {
    color: #FF4B4B;
    font-weight: bold;
}

h1, h2, h3 {
    color: #1E90FF;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 📌 SIDEBAR NAVIGASI
# =========================
menu = st.sidebar.radio(
    "📌 Menu EcoSurface",
    ["🏠 Beranda", "🧪 Panduan Sampling", "📊 Evaluasi Baku Mutu", "ℹ️ Tentang Aplikasi"]
)

# =========================
# 🏠 BERANDA
# =========================
if menu == "🏠 Beranda":

    st.title("🌊 EcoSurface")
    st.subheader("Sistem Pendukung Pemantauan Kualitas Air Permukaan")

    st.write("Aplikasi ini membantu dalam penentuan sampling dan evaluasi kualitas air berdasarkan baku mutu.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📦 Parameter Sampling", len(sampling_data))

    with col2:
        st.metric("⚖️ Parameter Baku Mutu", len(baku_mutu))

# =========================
# 🧪 PANDUAN SAMPLING
# =========================
elif menu == "🧪 Panduan Sampling":

    st.title("🧪 Panduan Sampling Air Permukaan")

    param = st.selectbox("Pilih Parameter", list(sampling_data.keys()))

    data = sampling_data[param]

    with st.container():
        st.markdown(f"""
        <div class="card">
        <h3>📌 {param}</h3>
        <p>🧴 Wadah: {data['wadah']}</p>
        <p>📦 Volume: {data['volume']}</p>
        <p>🧪 Pengawet: {data['pengawet']}</p>
        <p>❄️ Penyimpanan: {data['penyimpanan']}</p>
        <p>⏳ Holding Time: {data['holding_time']}</p>
        <p>📝 Catatan: {data['catatan']}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# 📊 EVALUASI BAKU MUTU
# =========================
elif menu == "📊 Evaluasi Baku Mutu":

    st.title("📊 Evaluasi Baku Mutu")

    param = st.selectbox("Pilih Parameter", list(baku_mutu.keys()))
    nilai = st.number_input("Masukkan Nilai Hasil Analisis")

    if st.button("Evaluasi"):

        batas = baku_mutu[param]

        # =========================
        # LOGIKA DO (MINIMUM)
        # =========================
        if param == "DO":
            if nilai >= batas:
                status = "✅ MEMENUHI BAKU MUTU"
                color = "good"
            else:
                status = "❌ TIDAK MEMENUHI BAKU MUTU"
                color = "bad"
        else:
            if nilai <= batas:
                status = "✅ MEMENUHI BAKU MUTU"
                color = "good"
            else:
                status = "❌ TIDAK MEMENUHI BAKU MUTU"
                color = "bad"

        selisih = abs(nilai - batas)

        st.markdown(f"""
        <div class="card">
        <h2 class="{color}">{status}</h2>
        <p>📌 Nilai Hasil: {nilai}</p>
        <p>⚖️ Baku Mutu: {batas}</p>
        <p>📏 Selisih: {selisih}</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# ℹ️ TENTANG
# =========================
elif menu == "ℹ️ Tentang Aplikasi":

    st.title("ℹ️ Tentang Aplikasi")

    st.markdown("""
    **Nama:** EcoSurface  

    **Deskripsi:**  
    Aplikasi pendukung pemantauan kualitas air permukaan yang membantu sampling, pengawetan, penyimpanan, dan evaluasi baku mutu.

    **Teknologi:**  
    - Python  
    - Streamlit  

    **Versi:** 1.0  

    **Developer:** Mahasiswa Politeknik AKA Bogor
    """)
# =========================
# 🧪 DATA SAMPLING PARAMETER
# =========================
sampling_data = {
    "COD": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "H2SO4 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Sampel harus segera didinginkan setelah pengambilan."
    },
    "BOD": {
        "wadah": "Botol kaca gelap",
        "volume": "300 mL",
        "pengawet": "Tidak boleh diawetkan",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Hindari kontak udara berlebih."
    },
    "TSS": {
        "wadah": "Botol PE",
        "volume": "1 L",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "7 hari",
        "catatan": "Sampel harus homogen."
    },
    "TDS": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "7 hari",
        "catatan": "Simpan tertutup rapat."
    }
}

# =========================
# ⚖️ BAKU MUTU
# =========================
baku_mutu = {
    "BOD": 3,
    "COD": 25,
    "TSS": 50,
    "TDS": 1000,
    "Nitrat": 10,
    "Nitrit": 0.06,
    "Amonia": 0.5,
    "Fosfat": 0.2,
    "Sulfat": 400,
    "Klorida": 600,
    "Besi (Fe)": 0.3,
    "Mangan (Mn)": 0.1,
    "DO": 4
}
    streamlit>=1.35.0
    # 🌊 EcoSurface

EcoSurface adalah aplikasi berbasis Streamlit untuk mendukung pemantauan kualitas air permukaan.

## ✨ Fitur
- Panduan sampling air
- Evaluasi baku mutu
- Dashboard sederhana
- UI modern dan responsif

## 🚀 Cara Menjalankan

```bash
pip install -r requirements.txt
streamlit run app.py
