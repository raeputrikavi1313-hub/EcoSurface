# ==========================================================
# ECOSURFACE
# Sistem Pendukung Pemantauan Kualitas Air Permukaan
# Developer : Mahasiswa Politeknik AKA Bogor
# Versi : 1.0
# ==========================================================

import streamlit as st
import pandas as pd

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================

st.set_page_config(
    page_title="EcoSurface",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* =======================================================
BACKGROUND
======================================================= */

.stApp{
    background: linear-gradient(
        180deg,
        #F4FFF8 0%,
        #F8FFFD 40%,
        #EEF8FF 100%
    );
}

/* =======================================================
HEADER
======================================================= */

.hero{
    background: linear-gradient(
        135deg,
        #2E8B57,
        #1E90FF
    );

    padding:30px;
    border-radius:22px;
    color:white;
    text-align:center;

    box-shadow:
    0px 6px 18px rgba(0,0,0,0.15);
}

/* =======================================================
CARD
======================================================= */

.info-card{

    background:white;

    border-radius:18px;

    padding:22px;

    margin-top:10px;

    box-shadow:
    0px 4px 12px rgba(0,0,0,0.08);

    border-left:6px solid #2E8B57;

    transition:0.3s;
}

.info-card:hover{

    transform:translateY(-3px);

    box-shadow:
    0px 8px 20px rgba(0,0,0,0.15);
}

/* =======================================================
SUCCESS CARD
======================================================= */

.success-card{

    background:#E8F5E9;

    border-left:8px solid #2E8B57;

    border-radius:18px;

    padding:22px;

    box-shadow:
    0px 4px 12px rgba(0,0,0,0.08);
}

/* =======================================================
DANGER CARD
======================================================= */

.danger-card{

    background:#FFEBEE;

    border-left:8px solid #D32F2F;

    border-radius:18px;

    padding:22px;

    box-shadow:
    0px 4px 12px rgba(0,0,0,0.08);
}

/* =======================================================
FOOTER
======================================================= */

.footer{

    text-align:center;

    color:#666;

    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# DATABASE PANDUAN SAMPLING
# ==========================================================

sampling_data = {

    "pH":{

        "wadah":"Botol PE",

        "volume":"250 mL",

        "pengawet":"Tidak perlu",

        "penyimpanan":"4°C",

        "holding_time":"Segera dianalisis",

        "catatan":"Pengukuran sebaiknya dilakukan sesegera mungkin."
    },

    "Suhu":{

        "wadah":"Botol PE",

        "volume":"Tidak diperlukan",

        "pengawet":"Tidak perlu",

        "penyimpanan":"In-situ",

        "holding_time":"Langsung diukur",

        "catatan":"Dilakukan langsung di lapangan."
    },

    "TSS":{

        "wadah":"Botol PE",

        "volume":"1000 mL",

        "pengawet":"Pendinginan 4°C",

        "penyimpanan":"4°C",

        "holding_time":"7 hari",

        "catatan":"Jangan disaring sebelum analisis."
    },

    "TDS":{

        "wadah":"Botol PE",

        "volume":"500 mL",

        "pengawet":"Pendinginan 4°C",

        "penyimpanan":"4°C",

        "holding_time":"7 hari",

        "catatan":"Simpan dalam kondisi tertutup."
    },

    "DO":{

        "wadah":"Botol Winkler",

        "volume":"300 mL",

        "pengawet":"MnSO₄ dan Alkali Iodida",

        "penyimpanan":"4°C",

        "holding_time":"8 jam",

        "catatan":"Hindari terbentuknya gelembung."
    },

    "BOD":{

        "wadah":"Botol PE",

        "volume":"1000 mL",

        "pengawet":"Pendinginan 4°C",

        "penyimpanan":"4°C",

        "holding_time":"48 jam",

        "catatan":"Analisis sesegera mungkin."
    },

    "COD":{

        "wadah":"Botol PE",

        "volume":"500 mL",

        "pengawet":"H₂SO₄ hingga pH < 2",

        "penyimpanan":"4°C",

        "holding_time":"28 hari",

        "catatan":"Segera didinginkan setelah sampling."
    },

    "Nitrat":{

        "wadah":"Botol PE",

        "volume":"500 mL",

        "pengawet":"Pendinginan 4°C",

        "penyimpanan":"4°C",

        "holding_time":"48 jam",

        "catatan":"Hindari kontaminasi pupuk."
    },

    "Nitrit":{

        "wadah":"Botol PE",

        "volume":"500 mL",

        "pengawet":"Pendinginan 4°C",

        "penyimpanan":"4°C",

        "holding_time":"48 jam",

        "catatan":"Simpan dalam pendingin."
    },

    "Amonia":{

        "wadah":"Botol PE",

        "volume":"500 mL",

        "pengawet":"H₂SO₄ hingga pH < 2",

        "penyimpanan":"4°C",

        "holding_time":"28 hari",

        "catatan":"Hindari paparan sinar matahari."
    },

    "Fosfat":{

        "wadah":"Botol PE",

        "volume":"500 mL",

        "pengawet":"Pendinginan 4°C",

        "penyimpanan":"4°C",

        "holding_time":"48 jam",

        "catatan":"Kocok perlahan sebelum analisis."
    },

    "Sulfat":{

        "wadah":"Botol PE",

        "volume":"500 mL",

        "pengawet":"Tidak perlu",

        "penyimpanan":"4°C",

        "holding_time":"28 hari",

        "catatan":"Simpan dalam wadah tertutup."
    },

    "Klorida":{

        "wadah":"Botol PE",

        "volume":"500 mL",

        "pengawet":"Tidak perlu",

        "penyimpanan":"4°C",

        "holding_time":"28 hari",

        "catatan":"Hindari kontaminasi garam."
    },
