EcoSurface/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── logo.png
│
└── data/
    └── parameter_data.py
# =====================================
# DATABASE PARAMETER SAMPLING
# =====================================

sampling_data = {
    "pH": {
        "wadah": "Botol PE",
        "volume": "250 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "Segera dianalisis",
        "catatan": "Hindari paparan panas."
    },

    "Suhu": {
        "wadah": "Botol PE",
        "volume": "-",
        "pengawet": "Tidak perlu",
        "penyimpanan": "In-situ",
        "holding_time": "Langsung diukur",
        "catatan": "Dilakukan di lapangan."
    },

    "DO": {
        "wadah": "Botol Winkler",
        "volume": "300 mL",
        "pengawet": "Fiksasi MnSO4",
        "penyimpanan": "4°C",
        "holding_time": "8 jam",
        "catatan": "Hindari gelembung udara."
    },

    "BOD": {
        "wadah": "Botol PE",
        "volume": "1000 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Analisis sesegera mungkin."
    },

    "COD": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "H2SO4 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Segera didinginkan."
    }
}

# =====================================
# DATABASE BAKU MUTU
# =====================================

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
         import streamlit as st
from data.parameter_data import sampling_data, baku_mutu

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="EcoSurface",
    page_icon="🌊",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    background-color: #F7FBFF;
}

.hero {
    background: linear-gradient(135deg,#2E8B57,#1E90FF);
    padding:25px;
    border-radius:20px;
    color:white;
    text-align:center;
    margin-bottom:20px;
}

.metric-card {
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
}

.info-card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    border-left:5px solid #1E90FF;
}

.success-card {
    background:#E8F5E9;
    padding:20px;
    border-radius:15px;
    border-left:6px solid green;
}

.danger-card {
    background:#FFEBEE;
    padding:20px;
    border-radius:15px;
    border-left:6px solid red;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

menu = st.sidebar.radio(
    "📌 Navigasi",
    [
        "🏠 Beranda",
        "🧪 Panduan Sampling",
        "📊 Evaluasi Baku Mutu",
        "ℹ️ Tentang Aplikasi"
    ]
)

# =====================================
# BERANDA
# =====================================

if menu == "🏠 Beranda":

    st.markdown("""
    <div class="hero">
    <h1>🌊 EcoSurface</h1>
    <h4>Sistem Pendukung Pemantauan Kualitas Air Permukaan</h4>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Parameter Sampling",
            len(sampling_data)
        )

    with col2:
        st.metric(
            "Parameter Baku Mutu",
            len(baku_mutu)
        )

    st.markdown("---")

    st.info("""
    EcoSurface membantu menentukan kebutuhan sampling,
    pengawetan sampel, holding time,
    serta evaluasi hasil analisis kualitas air.
    """)

# =====================================
# PANDUAN SAMPLING
# =====================================

elif menu == "🧪 Panduan Sampling":

    st.title("🧪 Panduan Sampling")

    parameter = st.selectbox(
        "Pilih Parameter",
        list(sampling_data.keys())
    )

    data = sampling_data[parameter]

    with st.container():

        st.markdown(f"""
        <div class="info-card">

        <h3>📌 {parameter}</h3>

        <b>🧴 Wadah</b><br>
        {data['wadah']}<br><br>

        <b>📏 Volume</b><br>
        {data['volume']}<br><br>

        <b>🧪 Pengawet</b><br>
        {data['pengawet']}<br><br>

        <b>❄️ Penyimpanan</b><br>
        {data['penyimpanan']}<br><br>

        <b>⏳ Holding Time</b><br>
        {data['holding_time']}<br><br>

        <b>📝 Catatan</b><br>
        {data['catatan']}

        </div>
        """, unsafe_allow_html=True)

# =====================================
# EVALUASI
# =====================================

elif menu == "📊 Evaluasi Baku Mutu":

    st.title("📊 Evaluasi Baku Mutu")

    parameter = st.selectbox(
        "Parameter",
        list(baku_mutu.keys())
    )

    nilai = st.number_input(
        "Hasil Analisis",
        min_value=0.0,
        value=0.0
    )

    if st.button("Evaluasi"):

        standar = baku_mutu[parameter]

        if parameter == "DO":
            memenuhi = nilai >= standar
        else:
            memenuhi = nilai <= standar

        selisih = abs(nilai - standar)

        if memenuhi:

            st.markdown(f"""
            <div class='success-card'>

            <h2>✅ MEMENUHI BAKU MUTU</h2>

            <b>Hasil Analisis :</b> {nilai}<br>
            <b>Baku Mutu :</b> {standar}<br>
            <b>Selisih :</b> {selisih}

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class='danger-card'>

            <h2>❌ TIDAK MEMENUHI BAKU MUTU</h2>

            <b>Hasil Analisis :</b> {nilai}<br>
            <b>Baku Mutu :</b> {standar}<br>
            <b>Selisih :</b> {selisih}

            </div>
            """, unsafe_allow_html=True)

# =====================================
# TENTANG
# =====================================

elif menu == "ℹ️ Tentang Aplikasi":

    st.title("ℹ️ Tentang Aplikasi")

    with st.expander("Informasi Aplikasi", expanded=True):

        st.markdown("""
        ### Nama Aplikasi
        EcoSurface

        ### Deskripsi
        Aplikasi pendukung kegiatan pemantauan kualitas air permukaan
        yang membantu menentukan kebutuhan sampling,
        pengawetan contoh,
        penyimpanan,
        holding time,
        serta evaluasi hasil analisis
        berdasarkan baku mutu.

        ### Teknologi
        - Python
        - Streamlit

        ### Versi
        1.0

        ### Developer
        Mahasiswa Politeknik AKA Bogor
        
        streamlit>=1.35.0
pandas>=2.2.2
# EcoSurface

Aplikasi Streamlit untuk pemantauan kualitas air permukaan.

## Fitur

- Panduan Sampling
- Evaluasi Baku Mutu
- Dashboard Ringkas
- UI Modern

## Instalasi

```bash
pip install -r requirements.txt
```

## Menjalankan

```bash
streamlit run app.py
```
