# 🚲 Bike Sharing Dashboard

Dashboard interaktif untuk menganalisis data penyewaan sepeda berdasarkan kondisi cuaca, musim, dan tipe pengguna.

## 📋 Deskripsi

Proyek ini adalah aplikasi dashboard yang dibangun menggunakan **Streamlit** untuk memvisualisasikan dan menganalisis data penyewaan sepeda. Data mencakup periode 2011-2012 dengan berbagai variabel seperti kondisi cuaca, musim, hari dalam seminggu, dan tipe pengguna (casual vs registered).

## 🛠️ Teknologi yang Digunakan

- **Streamlit** - Framework untuk membuat aplikasi web interaktif
- **Pandas** - Manipulasi dan analisis data
- **Plotly** - Library untuk membuat grafik interaktif
- **Statsmodels** - Untuk analisis statistik dan trendline

## 📁 Struktur Berkas

```
dashboard/
├── bike_sharing_dashboard.py  # File utama dashboard
├── day_clean.csv              # Data harian (sudah cleaning)
├── hour_clean.csv             # Data per jam (sudah cleaning)
├── requirements.txt           # Dependencies
└── README.md                  # Dokumentasi ini
```

## 🚀 Cara Menjalankan

### 1. Setup Environment (Virtual Environment)

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan Dashboard

```bash
# Masuk ke direktori dashboard (jika belum)
cd dashboard

# Jalankan Streamlit
streamlit run bike_sharing_dashboard.py
```

### 4. Buka Browser

Akses `http://localhost:8501` di browser Anda.

## 📊 Fitur Dashboard

### 1. Overview
- Rata-rata penyewaan berdasarkan kondisi cuaca
- Distribusi tipe pengguna (casual vs registered)

### 2. Cuaca & Musim
- Analisis pengaruh kondisi cuaca terhadap penyewaan
- Perbandingan penyewaan antar musim (Spring, Summer, Fall, Winter)
- Hubungan suhu vs penyewaan

### 3. Tren Waktu
- Tren penyewaan bulanan
- Proporsi casual vs registered per bulan

### 4. Analisis Lanjutan
- Correlation matrix antar variabel
- Kategori penyewaan (Low, Medium, High)

## 🔍 Filter Interaktif

Dashboard menyediakan filter berikut:
- **Kondisi Cuaca** - Clear, Cloudy, Drizzling, Heavy Rain
- **Musim** - Spring, Summer, Fall, Winter
- **Tahun** - 2011, 2012

> **Catatan:** Dashboard menampilkan visualisasi default menggunakan seluruh data tanpa perlu memilih filter terlebih dahulu.

## 📈 Variabel Data

| Variabel | Deskripsi |
|----------|-----------|
| `dteday` | Tanggal |
| `season` | Musim (1:Spring, 2:Summer, 3:Fall, 4:Winter) |
| `yr` | Tahun (0:2011, 1:2012) |
| `weathersit` | Kondisi cuaca |
| `casual` | Jumlah pengguna casual |
| `registered` | Jumlah pengguna registered |
| `cnt` | Total penyewaan |

## 📝 Lisensi

Proyek ini dibuat untuk tujuan edukasi dan analisis data.

## 👤 Author

Dashboard ini dibuat sebagai proyek analisis data penyewaan sepeda.