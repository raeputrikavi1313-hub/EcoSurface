import streamlit as st
import pandas as pd

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================

st.set_page_config(
    page_title="EcoSurface",
    page_icon="🌊",
    layout="wide"
)

# ==================================================
# CSS CUSTOM
# ==================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        180deg,
        #F4FFF8,
        #EEF8FF
    );
}

.hero{
    background: linear-gradient(
        135deg,
        #2E8B57,
        #1E90FF
    );
    padding:30px;
    border-radius:20px;
    color:white;
    text-align:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.15);
}

.info-card{
    background:white;
    padding:20px;
    border-radius:16px;
    box-shadow:0 3px 10px rgba(0,0,0,0.10);
    border-left:6px solid #1E90FF;
}

.success-card{
    background:#E8F5E9;
    padding:20px;
    border-radius:16px;
    border-left:8px solid #2E8B57;
}

.danger-card{
    background:#FFEBEE;
    padding:20px;
    border-radius:16px;
    border-left:8px solid #D32F2F;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# DATA SAMPLING
# ==================================================

sampling_data = {

    "pH": {
        "wadah": "Botol PE",
        "volume": "250 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "Segera dianalisis",
        "catatan": "Analisis dilakukan sesegera mungkin."
    },

    "Suhu": {
        "wadah": "Botol PE",
        "volume": "-",
        "pengawet": "Tidak perlu",
        "penyimpanan": "In-situ",
        "holding_time": "Langsung diukur",
        "catatan": "Diukur langsung di lapangan."
    },

    "TSS": {
        "wadah": "Botol PE",
        "volume": "1000 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "7 hari",
        "catatan": "Jangan disaring sebelum analisis."
    },

    "TDS": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "7 hari",
        "catatan": "Simpan tertutup rapat."
    },

    "DO": {
        "wadah": "Botol Winkler",
        "volume": "300 mL",
        "pengawet": "MnSO4",
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
    },

    "Nitrat": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Hindari kontaminasi pupuk."
    },

    "Nitrit": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Simpan dalam pendingin."
    },

    "Amonia": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "H2SO4 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Jauhkan dari sinar matahari."
    }
}
# ==================================================
# LANJUTAN DATA SAMPLING
# ==================================================

sampling_data.update({

    "Fosfat": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Pendinginan 4°C",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Kocok perlahan sebelum analisis."
    },

    "Sulfat": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "-"
    },

    "Klorida": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "-"
    },

    "Total Coliform": {
        "wadah": "Botol Steril",
        "volume": "100 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Jaga sterilitas wadah dan sampel."
    },

    "Fecal Coliform": {
        "wadah": "Botol Steril",
        "volume": "100 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Jaga sterilitas selama sampling."
    },

    "Besi (Fe)": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "HNO3 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "6 bulan",
        "catatan": "Gunakan wadah bebas logam."
    },

    "Mangan (Mn)": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "HNO3 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "6 bulan",
        "catatan": "Gunakan wadah bebas logam."
    }

})

# ==================================================
# DATA BAKU MUTU + SATUAN
# ==================================================

baku_mutu = {

    "BOD": {
        "nilai": 3,
        "satuan": "mg/L"
    },

    "COD": {
        "nilai": 25,
        "satuan": "mg/L"
    },

    "TSS": {
        "nilai": 50,
        "satuan": "mg/L"
    },

    "TDS": {
        "nilai": 1000,
        "satuan": "mg/L"
    },

    "Nitrat": {
        "nilai": 10,
        "satuan": "mg/L"
    },

    "Nitrit": {
        "nilai": 0.06,
        "satuan": "mg/L"
    },

    "Amonia": {
        "nilai": 0.5,
        "satuan": "mg/L"
    },

    "Fosfat": {
        "nilai": 0.2,
        "satuan": "mg/L"
    },

    "Sulfat": {
        "nilai": 400,
        "satuan": "mg/L"
    },

    "Klorida": {
        "nilai": 600,
        "satuan": "mg/L"
    },

    "Besi (Fe)": {
        "nilai": 0.3,
        "satuan": "mg/L"
    },

    "Mangan (Mn)": {
        "nilai": 0.1,
        "satuan": "mg/L"
    },

    "DO": {
        "nilai": 4,
        "satuan": "mg/L"
    }

}

# ==================================================
# SIDEBAR
# ==================================================

menu = st.sidebar.radio(
    "📋 Menu Navigasi",
    [
        "🏠 Beranda",
        "🧪 Panduan Sampling",
        "📊 Evaluasi Baku Mutu",
        "ℹ️ Tentang Aplikasi"
    ]
)

# ==================================================
# HALAMAN BERANDA
# ==================================================

if menu == "🏠 Beranda":

    st.markdown("""
    <div class="hero">
        <h1>🌊 EcoSurface</h1>
        <h3>Sistem Pendukung Pemantauan Kualitas Air Permukaan</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🧪 Parameter Sampling",
            len(sampling_data)
        )

    with col2:
        st.metric(
            "📊 Parameter Baku Mutu",
            len(baku_mutu)
        )

    st.write("")

    st.markdown("""
    <div class="info-card">

    <h3>🌿 Tentang EcoSurface</h3>

    EcoSurface membantu pengguna dalam:

    <br><br>

    ✅ Menentukan kebutuhan sampling air permukaan

    <br>

    ✅ Menentukan wadah dan bahan pengawet

    <br>

    ✅ Menentukan holding time

    <br>

    ✅ Mengevaluasi hasil analisis terhadap baku mutu

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("📋 Daftar Baku Mutu")

    df_baku_mutu = pd.DataFrame({
        "Parameter": baku_mutu.keys(),
        "Nilai": [v["nilai"] for v in baku_mutu.values()],
        "Satuan": [v["satuan"] for v in baku_mutu.values()]
    })

    st.dataframe(
        df_baku_mutu,
        use_container_width=True,
        hide_index=True
    )
    # ==================================================
# HALAMAN PANDUAN SAMPLING
# ==================================================

elif menu == "🧪 Panduan Sampling":

    st.title("🧪 Panduan Sampling Air Permukaan")

    st.write("""
    Pilih parameter kualitas air yang akan diuji.
    Sistem akan menampilkan kebutuhan sampling,
    pengawetan, penyimpanan, dan holding time.
    """)

    parameter = st.selectbox(
        "Pilih Parameter",
        list(sampling_data.keys())
    )

    data = sampling_data[parameter]

    st.write("")

    st.markdown(f"""
    <div class="info-card">

    <h2>📌 {parameter}</h2>

    <hr>

    🧴 <b>Jenis Wadah</b>

    <br>

    {data['wadah']}

    <br><br>

    📏 <b>Volume Minimum</b>

    <br>

    {data['volume']}

    <br><br>

    🧪 <b>Bahan Pengawet</b>

    <br>

    {data['pengawet']}

    <br><br>

    ❄️ <b>Suhu Penyimpanan</b>

    <br>

    {data['penyimpanan']}

    <br><br>

    ⏳ <b>Holding Time</b>

    <br>

    {data['holding_time']}

    <br><br>

    📝 <b>Catatan Tambahan</b>

    <br>

    {data['catatan']}

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    with st.expander("📚 Informasi Tambahan"):

        st.write(f"""
        Parameter yang dipilih adalah **{parameter}**.

        Pastikan pengambilan sampel dilakukan sesuai
        metode yang berlaku agar hasil analisis
        representatif dan akurat.
        """)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📦 Wadah",
            data["wadah"]
        )

    with col2:
        st.metric(
            "⏳ Holding Time",
            data["holding_time"]
        )
        import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# =========================
# 🌿 CONFIG UI KARTUN HIJAU
# =========================
st.set_page_config(page_title="EcoWater Monitor", layout="wide")

st.markdown(
    """
    <style>
    body {
        background-color: #e8fff1;
    }
    .main {
        background-color: #e8fff1;
    }
    h1 {
        color: #2e8b57;
        text-align: center;
    }
    .stButton>button {
        background-color: #2e8b57;
        color: white;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💧 EcoWater Monitor (Versi Kartun Hijau)")

# =========================
# 📊 DATABASE SEDERHANA
# =========================
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "Waktu", "pH", "Suhu", "TDS"
    ])

# =========================
# 📥 INPUT DATA
# =========================
st.header("📥 Input Kualitas Air")

col1, col2, col3 = st.columns(3)

with col1:
    ph = st.number_input("pH Air", 0.0, 14.0, 7.0)

with col2:
    suhu = st.number_input("Suhu (°C)", 0.0, 100.0, 25.0)

with col3:
    tds = st.number_input("TDS (ppm)", 0, 2000, 100)

if st.button("Simpan Data 🌱"):
    new_data = {
        "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pH": ph,
        "Suhu": suhu,
        "TDS": tds
    }

    st.session_state.data = pd.concat(
        [st.session_state.data, pd.DataFrame([new_data])],
        ignore_index=True
    )

    st.success("Data berhasil disimpan!")

# =========================
# 🧠 LOGIKA STATUS AIR
# =========================
def status_air(ph, suhu, tds):
    if 6.5 <= ph <= 8.5 and suhu <= 30 and tds <= 500:
        return "🟢 AMAN"
    elif 6.0 <= ph <= 9.0:
        return "🟡 WASPADA"
    else:
        return "🔴 BAHAYA"

if not st.session_state.data.empty:
    last = st.session_state.data.iloc[-1]
    status = status_air(last["pH"], last["Suhu"], last["TDS"])

    st.subheader("📌 Status Air Terbaru")
    st.markdown(f"### {status}")

# =========================
# 📊 VISUALISASI GRAFIK
# =========================
st.header("📊 Grafik Kualitas Air")

if not st.session_state.data.empty:
    fig, ax = plt.subplots()

    ax.plot(st.session_state.data["pH"], label="pH")
    ax.plot(st.session_state.data["Suhu"], label="Suhu")
    ax.plot(st.session_state.data["TDS"], label="TDS")

    ax.set_title("Perubahan Parameter Air")
    ax.legend()

    st.pyplot(fig)
else:
    st.info("Belum ada data untuk ditampilkan.")

# =========================
# 📁 TABEL DATA
# =========================
st.header("📁 Riwayat Data")

st.dataframe(st.session_state.data)
import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
import plotly.express as px

# =========================
# 🌿 UI THEME KARTUN HIJAU
# =========================
st.set_page_config(page_title="EcoWater Monitor Pro", layout="wide")

st.markdown("""
<style>
body { background-color: #e9fff2; }
h1 { color: #2e8b57; text-align: center; }
.sidebar .sidebar-content { background-color: #d9ffe8; }
.stButton>button {
    background-color: #2e8b57;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("💧 EcoWater Monitor PRO (Final Version)")

# =========================
# 🗄️ DATABASE SQLITE
# =========================
conn = sqlite3.connect("water.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS water_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    waktu TEXT,
    ph REAL,
    suhu REAL,
    tds REAL
)
""")
conn.commit()

# =========================
# 📥 SIDEBAR NAVIGASI
# =========================
menu = st.sidebar.selectbox(
    "📌 Menu",
    ["Input Data", "Dashboard", "Riwayat", "Download"]
)

# =========================
# 🧠 FUNGSI STATUS AIR
# =========================
def status_air(ph, suhu, tds):
    if 6.5 <= ph <= 8.5 and suhu <= 30 and tds <= 500:
        return "🟢 AMAN"
    elif 6.0 <= ph <= 9.0:
        return "🟡 WASPADA"
    else:
        return "🔴 BAHAYA"

# =========================
# 📥 INPUT DATA
# =========================
if menu == "Input Data":
    st.header("📥 Input Data Kualitas Air")

    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    suhu = st.number_input("Suhu (°C)", 0.0, 100.0, 25.0)
    tds = st.number_input("TDS (ppm)", 0, 2000, 100)

    if st.button("Simpan 🌱"):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        c.execute(
            "INSERT INTO water_data (waktu, ph, suhu, tds) VALUES (?, ?, ?, ?)",
            (waktu, ph, suhu, tds)
        )
        conn.commit()

        st.success("Data berhasil disimpan!")

        status = status_air(ph, suhu, tds)

        if "BAHAYA" in status:
            st.error("🚨 PERINGATAN! Kualitas air berbahaya!")
        elif "WASPADA" in status:
            st.warning("⚠️ Kualitas air tidak stabil!")
        else:
            st.success("✅ Air dalam kondisi aman!")

# =========================
# 📊 DASHBOARD
# =========================
elif menu == "Dashboard":
    st.header("📊 Dashboard Analisis")

    df = pd.read_sql("SELECT * FROM water_data", conn)

    if not df.empty:
        fig = px.line(df, x="waktu", y=["ph", "suhu", "tds"],
                      title="Tren Kualitas Air",
                      markers=True)
        st.plotly_chart(fig, use_container_width=True)

        last = df.iloc[-1]
        st.subheader("📌 Status Terbaru")

        status = status_air(last["ph"], last["suhu"], last["tds"])
        st.markdown(f"### {status}")

    else:
        st.info("Belum ada data.")

# =========================
# 📁 RIWAYAT DATA
# =========================
elif menu == "Riwayat":
    st.header("📁 Data Tersimpan")

    df = pd.read_sql("SELECT * FROM water_data", conn)
    st.dataframe(df)

# =========================
# 📥 DOWNLOAD LAPORAN
# =========================
elif menu == "Download":
    st.header("📥 Download Laporan CSV")

    df = pd.read_sql("SELECT * FROM water_data", conn)

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "⬇️ Download Data",
        csv,
        "laporan_kualitas_air.csv",
        "text/csv"
    )
