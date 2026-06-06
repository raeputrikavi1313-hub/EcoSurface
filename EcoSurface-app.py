import streamlit as st

# =========================
# ⚙️ SETTING HALAMAN
# =========================
st.set_page_config(
    page_title="EcoSurface",
    layout="centered"
)

# =========================
# 🌊 JUDUL
# =========================
st.title("🌊 EcoSurface")
st.subheader("Sistem Pendukung Pemantauan Kualitas Air Permukaan")

st.write("Aplikasi ini membantu panduan sampling dan evaluasi kualitas air.")

# =========================
# 📌 MENU SIDEBAR (SIMPLE)
# =========================
menu = st.sidebar.selectbox(
    "Menu",
    ["Beranda"]
)

# =========================
# 🏠 BERANDA
# =========================
if menu == "Beranda":

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Parameter Sampling", 16)

    with col2:
        st.metric("Parameter Baku Mutu", 13)

    st.info("EcoSurface versi awal berhasil dijalankan. Tahap berikutnya kita tambah fitur sampling dan evaluasi.")
import streamlit as st

# =========================
# ⚙️ SETTING
# =========================
st.set_page_config(
    page_title="EcoSurface",
    layout="centered"
)

# =========================
# 🧪 DATA SAMPLING (SIMPLE DI DALAM CODE BIAR GA ERROR)
# =========================
sampling_data = {
    "pH": {
        "wadah": "Botol plastik PE",
        "volume": "500 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Sampel harus segera dianalisis"
    },
    "COD": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "H2SO4 hingga pH < 2",
        "penyimpanan": "4°C",
        "holding_time": "28 hari",
        "catatan": "Dinginkan segera setelah sampling"
    },
    "BOD": {
        "wadah": "Botol kaca gelap",
        "volume": "300 mL",
        "pengawet": "Tidak boleh diawetkan",
        "penyimpanan": "4°C",
        "holding_time": "48 jam",
        "catatan": "Hindari udara masuk"
    },
    "TSS": {
        "wadah": "Botol PE",
        "volume": "1 L",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "7 hari",
        "catatan": "Homogenkan sampel"
    }
}

# =========================
# 🌊 JUDUL
# =========================
st.title("🌊 EcoSurface")
st.subheader("Sistem Pemantauan Kualitas Air Permukaan")

# =========================
# 📌 SIDEBAR MENU
# =========================
menu = st.sidebar.selectbox(
    "Menu",
    ["Beranda", "Panduan Sampling"]
)

# =========================
# 🏠 BERANDA
# =========================
if menu == "Beranda":

    st.metric("Parameter Sampling", len(sampling_data))
    st.info("Pilih menu Panduan Sampling untuk melihat detail.")

# =========================
# 🧪 PANDUAN SAMPLING
# =========================
elif menu == "Panduan Sampling":

    st.header("🧪 Panduan Sampling Air")

    parameter = st.selectbox("Pilih Parameter", list(sampling_data.keys()))

    data = sampling_data[parameter]

    st.markdown("### 📋 Detail Sampling")

    st.write("🧴 Wadah :", data["wadah"])
    st.write("📦 Volume :", data["volume"])
    st.write("🧪 Pengawet :", data["pengawet"])
    st.write("❄️ Penyimpanan :", data["penyimpanan"])
    st.write("⏳ Holding Time :", data["holding_time"])
    st.write("📝 Catatan :", data["catatan"])
    import streamlit as st

# =========================
# ⚙️ SETTING
# =========================
st.set_page_config(
    page_title="EcoSurface",
    layout="centered"
)

# =========================
# 🧪 DATA SAMPLING (DARI TAHAP 2)
# =========================
sampling_data = {
    "pH": {
        "wadah": "Botol plastik PE",
        "volume": "500 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Sampel harus segera dianalisis"
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
    "Fe": 0.3,
    "Mn": 0.1,
    "DO": 4
}

# =========================
# 🌊 JUDUL
# =========================
st.title("🌊 EcoSurface")
st.subheader("Sistem Pemantauan Kualitas Air Permukaan")

# =========================
# 📌 SIDEBAR MENU
# =========================
menu = st.sidebar.selectbox(
    "Menu",
    ["Beranda", "Panduan Sampling", "Evaluasi Baku Mutu"]
)

# =========================
# 🏠 BERANDA
# =========================
if menu == "Beranda":

    st.metric("Parameter Sampling", len(sampling_data))
    st.metric("Parameter Baku Mutu", len(baku_mutu))

    st.info("Gunakan menu Panduan Sampling atau Evaluasi Baku Mutu.")

# =========================
# 🧪 PANDUAN SAMPLING
# =========================
elif menu == "Panduan Sampling":

    st.header("🧪 Panduan Sampling")

    param = st.selectbox("Pilih Parameter", list(sampling_data.keys()))
    data = sampling_data[param]

    st.write("🧴 Wadah:", data["wadah"])
    st.write("📦 Volume:", data["volume"])
    st.write("🧪 Pengawet:", data["pengawet"])
    st.write("❄️ Penyimpanan:", data["penyimpanan"])
    st.write("⏳ Holding Time:", data["holding_time"])
    st.write("📝 Catatan:", data["catatan"])

# =========================
# 📊 EVALUASI BAKU MUTU
# =========================
elif menu == "Evaluasi Baku Mutu":

    st.header("📊 Evaluasi Baku Mutu Air")

    parameter = st.selectbox("Pilih Parameter", list(baku_mutu.keys()))
    nilai = st.number_input("Masukkan Nilai Hasil Analisis")

    if st.button("Evaluasi"):

        batas = baku_mutu[parameter]

        # =========================
        # LOGIKA DO (MINIMUM)
        # =========================
        if parameter == "DO":
            if nilai >= batas:
                status = "✅ MEMENUHI BAKU MUTU"
                st.success(status)
            else:
                status = "❌ TIDAK MEMENUHI BAKU MUTU"
                st.error(status)

        # =========================
        # PARAMETER MAKSIMUM
        # =========================
        else:
            if nilai <= batas:
                status = "✅ MEMENUHI BAKU MUTU"
                st.success(status)
            else:
                status = "❌ TIDAK MEMENUHI BAKU MUTU"
                st.error(status)

        # =========================
        # INFO HASIL
        # =========================
        st.write("📌 Nilai Anda :", nilai)
        st.write("⚖️ Baku Mutu :", batas)
        st.write("📏 Selisih :", abs(nilai - batas))
        import streamlit as st

# =========================
# ⚙️ CONFIG
# =========================
st.set_page_config(
    page_title="EcoSurface",
    layout="wide"
)

# =========================
# 🎨 CSS RINGAN (AMAN, TIDAK BERAT)
# =========================
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

.card {
    background-color: #ffffff;
    padding: 15px;
    border-radius: 12px;
    border-left: 5px solid #2E8B57;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🧪 DATA
# =========================
sampling_data = {
    "pH": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Segera analisis setelah sampling"
    }
}

baku_mutu = {
    "BOD": 3,
    "COD": 25,
    "TSS": 50,
    "TDS": 1000,
    "DO": 4
}

# =========================
# 🌊 HEADER
# =========================
st.title("🌊 EcoSurface")
st.caption("Sistem Pendukung Pemantauan Kualitas Air Permukaan")

# =========================
# 📌 SIDEBAR MENU
# =========================
menu = st.sidebar.radio(
    "Menu",
    ["Beranda", "Panduan Sampling", "Evaluasi Baku Mutu"]
)

# =========================
# 🏠 BERANDA
# =========================
if menu == "Beranda":

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Parameter Sampling", len(sampling_data))

    with col2:
        st.metric("Parameter Baku Mutu", len(baku_mutu))

    st.info("Pilih menu di sidebar untuk mulai analisis.")

# =========================
# 🧪 SAMPLING
# =========================
elif menu == "Panduan Sampling":

    st.header("🧪 Panduan Sampling")

    param = st.selectbox("Pilih Parameter", list(sampling_data.keys()))
    data = sampling_data[param]

    st.markdown(f"""
    <div class="card">
    <b>📌 Parameter:</b> {param}<br>
    <b>🧴 Wadah:</b> {data['wadah']}<br>
    <b>📦 Volume:</b> {data['volume']}<br>
    <b>🧪 Pengawet:</b> {data['pengawet']}<br>
    <b>❄️ Penyimpanan:</b> {data['penyimpanan']}<br>
    <b>⏳ Holding Time:</b> {data['holding_time']}<br>
    <b>📝 Catatan:</b> {data['catatan']}
    </div>
    """, unsafe_allow_html=True)

# =========================
# 📊 EVALUASI
# =========================
elif menu == "Evaluasi Baku Mutu":

    st.header("📊 Evaluasi Baku Mutu")

    param = st.selectbox("Pilih Parameter", list(baku_mutu.keys()))
    nilai = st.number_input("Masukkan Nilai")

    if st.button("Evaluasi"):

        batas = baku_mutu[param]

        # DO = minimum
        if param == "DO":
            memenuhi = nilai >= batas
        else:
            memenuhi = nilai <= batas

        selisih = abs(nilai - batas)

        if memenuhi:
            st.markdown(f"""
            <div class="card" style="border-left:5px solid #2E8B57;">
            <h3 style="color:#2E8B57;">✅ MEMENUHI BAKU MUTU</h3>
            <p>📌 Nilai: {nilai}</p>
            <p>⚖️ Baku Mutu: {batas}</p>
            <p>📏 Selisih: {selisih}</p>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
            <div class="card" style="border-left:5px solid #FF4B4B;">
            <h3 style="color:#FF4B4B;">❌ TIDAK MEMENUHI BAKU MUTU</h3>
            <p>📌 Nilai: {nilai}</p>
            <p>⚖️ Baku Mutu: {batas}</p>
            <p>📏 Selisih: {selisih}</p>
            </div>
            """, unsafe_allow_html=True)
            import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
import plotly.express as px

# =========================
# ⚙️ CONFIG
# =========================
st.set_page_config(
    page_title="EcoSurface",
    layout="wide"
)

# =========================
# 🗄️ DATABASE
# =========================
conn = sqlite3.connect("ecosurface.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS data_air (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    waktu TEXT,
    parameter TEXT,
    nilai REAL
)
""")
conn.commit()

# =========================
# 🧠 DATA
# =========================
sampling_data = {
    "pH": {
        "wadah": "Botol PE",
        "volume": "500 mL",
        "pengawet": "Tidak perlu",
        "penyimpanan": "4°C",
        "holding_time": "24 jam",
        "catatan": "Segera analisis"
    }
}

baku_mutu = {
    "BOD": 3,
    "COD": 25,
    "TSS": 50,
    "TDS": 1000,
    "DO": 4
}

# =========================
# 🎨 UI HEADER
# =========================
st.title("🌊 EcoSurface")
st.caption("Sistem Pendukung Pemantauan Kualitas Air Permukaan")

# =========================
# 📌 MENU
# =========================
menu = st.sidebar.radio(
    "Menu",
    ["Beranda", "Panduan Sampling", "Evaluasi", "Dashboard"]
)

# =========================
# 🏠 BERANDA
# =========================
if menu == "Beranda":

    col1, col2 = st.columns(2)

    col1.metric("Sampling Parameter", len(sampling_data))
    col2.metric("Baku Mutu Parameter", len(baku_mutu))

    st.info("Gunakan menu untuk mulai analisis.")

# =========================
# 🧪 SAMPLING
# =========================
elif menu == "Panduan Sampling":

    st.header("🧪 Panduan Sampling")

    param = st.selectbox("Pilih Parameter", list(sampling_data.keys()))
    data = sampling_data[param]

    st.write("🧴 Wadah:", data["wadah"])
    st.write("📦 Volume:", data["volume"])
    st.write("🧪 Pengawet:", data["pengawet"])
    st.write("❄️ Penyimpanan:", data["penyimpanan"])
    st.write("⏳ Holding Time:", data["holding_time"])
    st.write("📝 Catatan:", data["catatan"])

# =========================
# 📊 EVALUASI
# =========================
elif menu == "Evaluasi":

    st.header("📊 Evaluasi Baku Mutu")

    param = st.selectbox("Parameter", list(baku_mutu.keys()))
    nilai = st.number_input("Nilai Hasil Analisis")

    if st.button("Simpan & Evaluasi"):

        batas = baku_mutu[param]
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # SIMPAN KE DATABASE
        c.execute(
            "INSERT INTO data_air (waktu, parameter, nilai) VALUES (?, ?, ?)",
            (waktu, param, nilai)
        )
        conn.commit()

        # LOGIKA
        if param == "DO":
            status = nilai >= batas
        else:
            status = nilai <= batas

        selisih = abs(nilai - batas)

        if status:
            st.success("✅ MEMENUHI BAKU MUTU")
        else:
            st.error("❌ TIDAK MEMENUHI BAKU MUTU")

        st.write("📌 Nilai:", nilai)
        st.write("⚖️ Baku Mutu:", batas)
        st.write("📏 Selisih:", selisih)

# =========================
# 📊 DASHBOARD
# =========================
elif menu == "Dashboard":

    st.header("📊 Dashboard Data")

    df = pd.read_sql("SELECT * FROM data_air", conn)

    if not df.empty:

        fig = px.line(df, x="waktu", y="nilai", color="parameter", markers=True)
        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇️ Download Data CSV",
            csv,
            "data_ecosurface.csv",
            "text/csv"
        )

    else:
        st.info("Belum ada data tersimpan")
