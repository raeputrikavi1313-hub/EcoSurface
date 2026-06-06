import streamlit as st

st.set_page_config(
    page_title="EcoSurface",
    page_icon="💧",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>
.main {
    background-color: #F4FFF8;
}

.card {
    background: white;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #2E8B57;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

.success-card{
    background:#E8F5E9;
    padding:20px;
    border-radius:15px;
    border-left:8px solid green;
}

.danger-card{
    background:#FFEBEE;
    padding:20px;
    border-radius:15px;
    border-left:8px solid red;
}
</style>
""", unsafe_allow_html=True)

# =========================
# DATABASE SAMPLING
# =========================

sampling_data = {
    "pH":{
        "wadah":"Botol PE",
        "volume":"250 mL",
        "pengawet":"Tidak perlu",
        "suhu":"4°C",
        "holding":"Segera dianalisis",
        "catatan":"Hindari paparan panas."
    },

    "Suhu":{
        "wadah":"Botol PE",
        "volume":"Tidak diperlukan",
        "pengawet":"Tidak perlu",
        "suhu":"In-situ",
        "holding":"Langsung diukur",
        "catatan":"Ukur di lapangan."
    },

    "TSS":{
        "wadah":"Botol PE",
        "volume":"1000 mL",
        "pengawet":"4°C",
        "suhu":"4°C",
        "holding":"7 hari",
        "catatan":"Jangan disaring."
    },

    "TDS":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"4°C",
        "suhu":"4°C",
        "holding":"7 hari",
        "catatan":"Simpan tertutup."
    },

    "DO":{
        "wadah":"Botol Winkler",
        "volume":"300 mL",
        "pengawet":"Fiksasi MnSO4",
        "suhu":"4°C",
        "holding":"8 jam",
        "catatan":"Hindari gelembung."
    },

    "BOD":{
        "wadah":"Botol PE",
        "volume":"1000 mL",
        "pengawet":"4°C",
        "suhu":"4°C",
        "holding":"48 jam",
        "catatan":"Analisis sesegera mungkin."
    },

    "COD":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"H2SO4 hingga pH<2",
        "suhu":"4°C",
        "holding":"28 hari",
        "catatan":"Segera dinginkan."
    },

    "Nitrat":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"4°C",
        "suhu":"4°C",
        "holding":"48 jam",
        "catatan":"Hindari kontaminasi."
    },

    "Nitrit":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"4°C",
        "suhu":"4°C",
        "holding":"48 jam",
        "catatan":"Simpan dingin."
    },

    "Amonia":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"H2SO4 pH<2",
        "suhu":"4°C",
        "holding":"28 hari",
        "catatan":"Jangan terkena matahari."
    },

    "Fosfat":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"4°C",
        "suhu":"4°C",
        "holding":"48 jam",
        "catatan":"Kocok sebelum analisis."
    },

    "Sulfat":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"Tidak perlu",
        "suhu":"4°C",
        "holding":"28 hari",
        "catatan":"-"
    },

    "Klorida":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"Tidak perlu",
        "suhu":"4°C",
        "holding":"28 hari",
        "catatan":"-"
    },

    "Total Coliform":{
        "wadah":"Botol Steril",
        "volume":"100 mL",
        "pengawet":"Tidak perlu",
        "suhu":"4°C",
        "holding":"24 jam",
        "catatan":"Jaga sterilitas."
    },

    "Fecal Coliform":{
        "wadah":"Botol Steril",
        "volume":"100 mL",
        "pengawet":"Tidak perlu",
        "suhu":"4°C",
        "holding":"24 jam",
        "catatan":"Jaga sterilitas."
    },

    "Besi (Fe)":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"HNO3 pH<2",
        "suhu":"4°C",
        "holding":"6 bulan",
        "catatan":"Gunakan wadah bebas logam."
    },

    "Mangan (Mn)":{
        "wadah":"Botol PE",
        "volume":"500 mL",
        "pengawet":"HNO3 pH<2",
        "suhu":"4°C",
        "holding":"6 bulan",
        "catatan":"Gunakan wadah bebas logam."
    }
}

# =========================
# BAKU MUTU
# =========================

baku_mutu = {
    "BOD":3,
    "COD":25,
    "TSS":50,
    "TDS":1000,
    "Nitrat":10,
    "Nitrit":0.06,
    "Amonia":0.5,
    "Fosfat":0.2,
    "Sulfat":400,
    "Klorida":600,
    "Besi (Fe)":0.3,
    "Mangan (Mn)":0.1,
    "DO":4
}

# =========================
# SIDEBAR
# =========================

menu = st.sidebar.radio(
    "📋 Menu",
    [
        "Beranda",
        "Panduan Sampling",
        "Evaluasi Baku Mutu",
        "Tentang Aplikasi"
    ]
)

# =========================
# BERANDA
# =========================

if menu == "Beranda":

    st.title("💧 EcoSurface")

    c1,c2 = st.columns(2)

    c1.metric(
        "Parameter Sampling",
        len(sampling_data)
    )

    c2.metric(
        "Parameter Baku Mutu",
        len(baku_mutu)
    )

# =========================
# PANDUAN SAMPLING
# =========================

elif menu == "Panduan Sampling":

    st.title("🧪 Panduan Sampling")

    parameter = st.selectbox(
        "Pilih Parameter",
        list(sampling_data.keys())
    )

    data = sampling_data[parameter]

    st.markdown(f"""
    <div class="card">
    <h3>{parameter}</h3>

    <b>Wadah:</b> {data['wadah']}<br>
    <b>Volume:</b> {data['volume']}<br>
    <b>Pengawet:</b> {data['pengawet']}<br>
    <b>Penyimpanan:</b> {data['suhu']}<br>
    <b>Holding Time:</b> {data['holding']}<br>
    <b>Catatan:</b> {data['catatan']}
    </div>
    """, unsafe_allow_html=True)

# =========================
# EVALUASI
# =========================

elif menu == "Evaluasi Baku Mutu":

    st.title("📊 Evaluasi Baku Mutu")

    parameter = st.selectbox(
        "Parameter",
        list(baku_mutu.keys())
    )

    nilai = st.number_input(
        "Nilai Analisis",
        min_value=0.0
    )

    if st.button("Evaluasi"):

        standar = baku_mutu[parameter]

        if parameter == "DO":
            status = nilai >= standar
        else:
            status = nilai <= standar

        selisih = abs(nilai - standar)

        if status:
            st.success(
                f"✅ Memenuhi Baku Mutu\n\nNilai: {nilai}\nBaku Mutu: {standar}\nSelisih: {selisih}"
            )
        else:
            st.error(
                f"❌ Tidak Memenuhi Baku Mutu\n\nNilai: {nilai}\nBaku Mutu: {standar}\nSelisih: {selisih}"
            )

# =========================
# TENTANG
# =========================

else:

    st.title("ℹ️ Tentang Aplikasi")

    st.write("""
    EcoSurface adalah aplikasi pendukung
    pemantauan kualitas air permukaan.

    Teknologi:
    • Python
    • Streamlit
    """)
