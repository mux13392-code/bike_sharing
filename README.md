# 🚲 Bike Sharing Dashboard

Dashboard interaktif untuk menganalisis data penyewaan sepeda berdasarkan kondisi cuaca, musim, dan tipe pengguna.

## 📋 Deskripsi

Proyek ini adalah aplikasi dashboard yang dibangun menggunakan **Streamlit** untuk memvisualisasikan dan menganalisis data penyewaan sepeda. Data mencakup periode 2011-2012 dengan berbagai variabel seperti kondisi cuaca, musim, hari dalam seminggu, dan tipe pengguna (casual vs registered).

## 🛠️ Teknologi yang Digunakan

- **Streamlit** - Framework untuk membuat aplikasi web interaktif
- **Pandas** - Manipulasi dan analisis data
- **Seaborn** - Visualisasi data statistik
- **Matplotlib** - Plotting library untuk Python
- **Plotly** - Library untuk membuat grafik interaktif

## 📁 Struktur Berkas

```
dashboard/
├── bike_sharing_dashboard.py  # File utama dashboard
├── day.csv                    # Data harian
├── hour.csv                   # Data per jam
├── requirements.txt           # Dependencies
└── README.md                  # Dokumentasi ini
```

## 🚀 Cara Menjalankan

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan dashboard:**
   ```bash
   streamlit run bike_sharing_dashboard.py
   ```

3. Buka browser dan akses `http://localhost:8501`

## 📊 Fitur Dashboard

### 1. Overview
- Rata-rata penyewaan berdasarkan kondisi cuaca
- Distribusi tipe pengguna (casual vs registered)

### 2. Cuaca & Musim
- Analisis pengaruh kondisi cuaca terhadap penyewaan
- Perbandingan penyewaan antar musim (Spring, Summer, Fall, Winter)

### 3. Tren Waktu
- Tren penyewaan harian
- Pola penyewaan berdasarkan hari dalam seminggu

### 4. Analisis Lanjutan
- Analisis korelasi antar variabel
- Visualisasi data yang lebih detail

## 🔍 Filter Interaktif

Dashboard menyediakan filter berikut:
- **Rentang Tanggal** - Filter berdasarkan periode waktu
- **Kondisi Cuaca** - Clear, Cloudy, Drizzling, Heavy Rain
- **Musim** - Spring, Summer, Fall, Winter
- **Tahun** - 2011, 2012

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