import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# ⚙️ SETTING HALAMAN (BIAR RAPI)
# =========================
st.set_page_config(
    page_title="EcoWater",
    layout="centered"
)

# =========================
# 🧠 DATA TEMPORARY
# =========================
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Waktu", "pH", "Suhu", "TDS"]
    )

# =========================
# 🌿 JUDUL
# =========================
st.title("💧 EcoWater Monitor")

st.write("Input sederhana kualitas air")

# =========================
# 📥 INPUT (DIBUAT COMPACT)
# =========================
ph = st.number_input("pH", 0.0, 14.0, 7.0)
suhu = st.number_input("Suhu (°C)", 0.0, 100.0, 25.0)
tds = st.number_input("TDS (ppm)", 0, 2000, 100)

# =========================
# 💾 SIMPAN DATA
# =========================
if st.button("Simpan"):
    data_baru = {
        "Waktu": datetime.now().strftime("%H:%M:%S"),
        "pH": ph,
        "Suhu": suhu,
        "TDS": tds
    }

    st.session_state.data = pd.concat(
        [st.session_state.data, pd.DataFrame([data_baru])],
        ignore_index=True
    )

    st.success("Tersimpan!")

# =========================
# 📁 TAMPILAN DATA
# =========================
st.subheader("Data Masuk")

st.dataframe(
    st.session_state.data,
    use_container_width=True
)
import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# ⚙️ SETTING HALAMAN
# =========================
st.set_page_config(
    page_title="EcoWater",
    layout="centered"
)

# =========================
# 🧠 DATA
# =========================
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Waktu", "pH", "Suhu", "TDS"]
    )

# =========================
# 🌿 JUDUL
# =========================
st.title("💧 EcoWater Monitor")

st.write("Monitoring kualitas air sederhana")

# =========================
# 📥 INPUT
# =========================
ph = st.number_input("pH", 0.0, 14.0, 7.0)
suhu = st.number_input("Suhu (°C)", 0.0, 100.0, 25.0)
tds = st.number_input("TDS (ppm)", 0, 2000, 100)

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
# 💾 SIMPAN DATA
# =========================
if st.button("Simpan"):
    status = status_air(ph, suhu, tds)

    data_baru = {
        "Waktu": datetime.now().strftime("%H:%M:%S"),
        "pH": ph,
        "Suhu": suhu,
        "TDS": tds
    }

    st.session_state.data = pd.concat(
        [st.session_state.data, pd.DataFrame([data_baru])],
        ignore_index=True
    )

    st.success("Data tersimpan!")

    # =========================
    # 📌 STATUS LANGSUNG MUNCUL
    # =========================
    st.subheader("Status Air")

    if status == "🟢 AMAN":
        st.success(status)
    elif status == "🟡 WASPADA":
        st.warning(status)
    else:
        st.error(status)

# =========================
# 📁 DATA
# =========================
st.subheader("Riwayat Data")

st.dataframe(
    st.session_state.data,
    use_container_width=True
)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# =========================
# ⚙️ SETTING HALAMAN
# =========================
st.set_page_config(
    page_title="EcoWater",
    layout="centered"
)

# =========================
# 🧠 DATA
# =========================
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Waktu", "pH", "Suhu", "TDS"]
    )

# =========================
# 🌿 JUDUL
# =========================
st.title("💧 EcoWater Monitor")
st.write("Monitoring kualitas air sederhana")

# =========================
# 📥 INPUT
# =========================
ph = st.number_input("pH", 0.0, 14.0, 7.0)
suhu = st.number_input("Suhu (°C)", 0.0, 100.0, 25.0)
tds = st.number_input("TDS (ppm)", 0, 2000, 100)

# =========================
# 🧠 FUNGSI STATUS
# =========================
def status_air(ph, suhu, tds):
    if 6.5 <= ph <= 8.5 and suhu <= 30 and tds <= 500:
        return "🟢 AMAN"
    elif 6.0 <= ph <= 9.0:
        return "🟡 WASPADA"
    else:
        return "🔴 BAHAYA"

# =========================
# 💾 SIMPAN DATA
# =========================
if st.button("Simpan"):
    status = status_air(ph, suhu, tds)

    data_baru = {
        "Waktu": datetime.now().strftime("%H:%M:%S"),
        "pH": ph,
        "Suhu": suhu,
        "TDS": tds
    }

    st.session_state.data = pd.concat(
        [st.session_state.data, pd.DataFrame([data_baru])],
        ignore_index=True
    )

    st.success("Data tersimpan!")

    # STATUS
    if status == "🟢 AMAN":
        st.success(status)
    elif status == "🟡 WASPADA":
        st.warning(status)
    else:
        st.error(status)

# =========================
# 📊 GRAFIK (TAHAP 3)
# =========================
st.subheader("📊 Grafik Monitoring")

if not st.session_state.data.empty:

    fig, ax = plt.subplots()

    ax.plot(st.session_state.data["pH"], label="pH")
    ax.plot(st.session_state.data["Suhu"], label="Suhu")
    ax.plot(st.session_state.data["TDS"], label="TDS")

    ax.set_title("Perubahan Kualitas Air")
    ax.legend()

    st.pyplot(fig)

else:
    st.info("Belum ada data untuk grafik.")

# =========================
# 📁 DATA
# =========================
st.subheader("Riwayat Data")

st.dataframe(
    st.session_state.data,
    use_container_width=True
)
import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# =========================
# ⚙️ SETTING
# =========================
st.set_page_config(
    page_title="EcoWater Pro",
    layout="wide"
)

# =========================
# 🧠 DATA
# =========================
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Waktu", "pH", "Suhu", "TDS"]
    )

# =========================
# 🧠 STATUS AIR
# =========================
def status_air(ph, suhu, tds):
    if 6.5 <= ph <= 8.5 and suhu <= 30 and tds <= 500:
        return "🟢 AMAN"
    elif 6.0 <= ph <= 9.0:
        return "🟡 WASPADA"
    else:
        return "🔴 BAHAYA"

# =========================
# 📌 SIDEBAR MENU
# =========================
menu = st.sidebar.selectbox(
    "📌 Menu",
    ["Input Data", "Dashboard", "Riwayat"]
)

# =========================
# 🌿 INPUT DATA
# =========================
if menu == "Input Data":

    st.title("💧 Input Data")

    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    suhu = st.number_input("Suhu (°C)", 0.0, 100.0, 25.0)
    tds = st.number_input("TDS (ppm)", 0, 2000, 100)

    if st.button("Simpan"):
        waktu = datetime.now().strftime("%H:%M:%S")

        st.session_state.data = pd.concat(
            [st.session_state.data, pd.DataFrame([{
                "Waktu": waktu,
                "pH": ph,
                "Suhu": suhu,
                "TDS": tds
            }])],
            ignore_index=True
        )

        st.success("Data tersimpan!")

        status = status_air(ph, suhu, tds)

        if status == "🟢 AMAN":
            st.success(status)
        elif status == "🟡 WASPADA":
            st.warning(status)
        else:
            st.error(status)

# =========================
# 📊 DASHBOARD
# =========================
elif menu == "Dashboard":

    st.title("📊 Dashboard Monitoring")

    if not st.session_state.data.empty:

        fig = px.line(
            st.session_state.data,
            x="Waktu",
            y=["pH", "Suhu", "TDS"],
            markers=True,
            title="Grafik Kualitas Air"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Belum ada data")

# =========================
# 📁 RIWAYAT
# =========================
elif menu == "Riwayat":

    st.title("📁 Data Tersimpan")

    st.dataframe(
        st.session_state.data,
        use_container_width=True
    )
    import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
import plotly.express as px

# =========================
# ⚙️ SETTING
# =========================
st.set_page_config(
    page_title="EcoWater Final",
    layout="wide"
)

# =========================
# 🗄️ DATABASE SQLITE
# =========================
conn = sqlite3.connect("water.db", check_same_thread=False)
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
# 🧠 STATUS AIR
# =========================
def status_air(ph, suhu, tds):
    if 6.5 <= ph <= 8.5 and suhu <= 30 and tds <= 500:
        return "🟢 AMAN"
    elif 6.0 <= ph <= 9.0:
        return "🟡 WASPADA"
    else:
        return "🔴 BAHAYA"

# =========================
# 📌 MENU SIDEBAR
# =========================
menu = st.sidebar.selectbox(
    "📌 Menu",
    ["Input Data", "Dashboard", "Riwayat", "Download"]
)

# =========================
# 📥 INPUT DATA
# =========================
if menu == "Input Data":

    st.title("💧 Input Data Kualitas Air")

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

        status = status_air(ph, suhu, tds)

        st.success("Data tersimpan!")

        # 🚨 ALARM
        if status == "🔴 BAHAYA":
            st.error("🚨 KUALITAS AIR BERBAHAYA!")
        elif status == "🟡 WASPADA":
            st.warning("⚠️ Kualitas air tidak stabil")
        else:
            st.success("🟢 Air dalam kondisi aman")

# =========================
# 📊 DASHBOARD
# =========================
elif menu == "Dashboard":

    st.title("📊 Dashboard Monitoring")

    df = pd.read_sql("SELECT * FROM water_data", conn)

    if not df.empty:

        fig = px.line(
            df,
            x="waktu",
            y=["ph", "suhu", "tds"],
            markers=True,
            title="Grafik Kualitas Air"
        )

        st.plotly_chart(fig, use_container_width=True)

        last = df.iloc[-1]
        status = status_air(last["ph"], last["suhu"], last["tds"])

        st.subheader("📌 Status Terbaru")
        st.markdown(f"### {status}")

    else:
        st.info("Belum ada data")

# =========================
# 📁 RIWAYAT
# =========================
elif menu == "Riwayat":

    st.title("📁 Data Tersimpan")

    df = pd.read_sql("SELECT * FROM water_data", conn)

    st.dataframe(df, use_container_width=True)

# =========================
# 📥 DOWNLOAD CSV
# =========================
elif menu == "Download":

    st.title("📥 Download Laporan")

    df = pd.read_sql("SELECT * FROM water_data", conn)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download CSV",
        csv,
        "laporan_air.csv",
        "text/csv"
    )
