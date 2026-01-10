
# SIAB Stock Prediction System

Sistem prediksi saham BBCA berbasis web, menggunakan model XGBoost yang terintegrasi penuh dengan Django. Sistem ini mendukung prediksi manual, batch (CSV), visualisasi, dan riwayat prediksi yang tersimpan di database.

## 📋 Deskripsi

SIAB Stock Prediction adalah aplikasi web yang memanfaatkan model XGBoost terlatih untuk memprediksi pergerakan harga saham BBCA (Bank Central Asia). Sistem menerima input data saham (manual/CSV), menghitung technical indicators, dan memberikan prediksi naik/turun beserta confidence dan rekomendasi aksi (BUY/SELL/HOLD).

## ✨ Fitur Utama

- **Prediksi Manual**: Input data saham secara manual, hasil prediksi langsung tampil.
- **Prediksi CSV**: Upload file CSV, sistem otomatis menghitung indikator teknikal dan memproses prediksi batch.
- **Visualisasi**: Tersedia chart interaktif (line, bar, pie) untuk analisis data dan hasil prediksi.
- **Riwayat Prediksi**: Semua prediksi tersimpan, dapat dilihat dan dikelola di halaman riwayat.
- **REST API**: Endpoint API untuk integrasi eksternal (lihat dokumentasi endpoint di bawah).
- **Admin Panel**: Kelola data, prediksi, dan user melalui Django Admin.

## 🛠️ Teknologi

- **Backend**: Django 5.x
- **Machine Learning**: XGBoost, scikit-learn
- **Data Processing**: Pandas, NumPy
- **Frontend**: Bootstrap 5, Chart.js, HTML5, CSS3
- **Database**: SQLite (default, bisa diubah ke PostgreSQL/MySQL)

## 🚀 Alur Kerja Sistem

1. User menginput data saham (manual/CSV) melalui web.
2. Sistem menghitung technical indicators (MA5, MA10, Return, Return_1, MA_diff).
3. Data diformat sesuai fitur model, lalu diprediksi menggunakan XGBoost (model hasil training di notebook).
4. Hasil prediksi (label, probability, rekomendasi aksi) ditampilkan dan disimpan ke database.
5. User dapat melihat riwayat, visualisasi, dan mengunduh hasil prediksi.

## 📦 Instalasi & Menjalankan

1. Clone/download project ke komputer Anda.
2. Install dependencies: `pip install -r requirements.txt`
3. Migrasi database: `python manage.py migrate`
4. (Opsional) Buat superuser: `python manage.py createsuperuser`
5. Jalankan server: `python manage.py runserver`
6. Akses di browser: http://localhost:8000

## 📖 Cara Penggunaan

### Prediksi Manual
1. Pilih menu "Prediksi Manual"
2. Isi semua field (Open, High, Low, Close, Volume, MA5, MA10, Return, Return_1, MA_diff)
3. Klik "Prediksi Sekarang" dan lihat hasil

### Prediksi CSV
1. Pilih menu "Upload CSV"
2. Upload file CSV sesuai format
3. Sistem otomatis menghitung indikator dan memproses prediksi

### Visualisasi
1. Pilih menu "Visualisasi"
2. Lihat chart interaktif dan analisis data

### Riwayat Prediksi
1. Pilih menu "Riwayat Prediksi"
2. Lihat, hapus, atau kelola hasil prediksi sebelumnya

### API Endpoint

**POST** `/api/predict/`

Request body:
```json
{
  "Open": 10000,
  "High": 10500,
  "Low": 9800,
  "Close": 10200,
  "Volume": 50000000,
  "MA5": 10100,
  "MA10": 10050,
  "Return": 0.005,
  "Return_1": 0.003,
  "MA_diff": 50
}
```

Response:
```json
{
  "success": true,
  "prediction": {
    "label": 1,
    "label_text": "Naik",
    "probability": 85.5,
    "probability_naik": 85.5,
    "probability_turun": 14.5
  }
}
```

## 📁 Struktur Project

```
CBL-SIAB/
├── siab_project/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── stock_prediction/          # Main app (ML, views, forms, templates)
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── ml_model.py
│   ├── admin.py
│   ├── urls.py
│   └── templates/
├── data/                      # Dataset folder
│   └── BBCA.JK_extended.csv
├── siab_model.pkl             # Trained XGBoost model
├── manage.py
├── requirements.txt
└── README.md
```

## 🎓 Model Information

- **Model**: XGBoost Classifier (hasil training dari notebook)
- **Fitur**: Open, High, Low, Close, Volume, MA5, MA10, Return, Return_1, MA_diff
- **Target**: 0=Turun, 1=Naik
- **Threshold**: 0.3% (0.003)
- **Parameter utama**: n_estimators=200, max_depth=6, learning_rate=0.05

## 🔧 Konfigurasi Penting

- Edit `siab_project/settings.py` untuk:
  - `MODEL_PATH`: Path file model `.pkl`
  - `DATA_PATH`: Path folder data
  - `DATABASES`: Ganti ke PostgreSQL/MySQL jika perlu
  - `ALLOWED_HOSTS`, `DEBUG`, dll

## 🐛 Troubleshooting

- Model tidak bisa di-load: pastikan file `siab_model.pkl` ada dan dependencies terinstall
- Error upload CSV: pastikan format dan kolom sesuai
- Chart tidak muncul: pastikan koneksi internet aktif (CDN)

## 📝 License

Project ini dibuat untuk pembelajaran dan penelitian.

---

**Selamat menggunakan SIAB Stock Prediction System!** 🚀

## 📦 Instalasi

### 1. Clone atau Download Project

```bash
cd C:\Users\putri\SIAB_CBL
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Migrasi Database

```bash
python manage.py migrate
```

### 4. Buat Superuser (Opsional)

```bash
python manage.py createsuperuser
```

### 5. Jalankan Server

```bash
python manage.py runserver
```

Akses aplikasi di: **http://localhost:8000**

## 📖 Cara Penggunaan

### 1. Prediksi Manual

1. Klik menu **"Prediksi Manual"**
2. Isi semua field yang diperlukan:
   - Open, High, Low, Close Price
   - Volume
   - Technical Indicators (MA5, MA10, Return, Return_1, MA_diff)
3. Klik **"Prediksi Sekarang"**
4. Lihat hasil prediksi dan confidence level

### 2. Upload CSV

1. Klik menu **"Upload CSV"**
2. Pilih file CSV dengan format:
   ```
   Date,Open,High,Low,Close,Volume
   2024-01-01,10000,10500,9800,10200,50000000
   ```
3. Klik **"Upload dan Prediksi"**
4. Sistem akan otomatis menghitung technical indicators dan membuat prediksi

### 3. Visualisasi

1. Klik menu **"Visualisasi"**
2. Lihat berbagai chart:
   - Line chart harga saham
   - Pie chart distribusi prediksi
   - Bar chart confidence level

### 4. API Endpoint

**POST** `/api/predict/`

Request body:
```json
{
  "Open": 10000,
  "High": 10500,
  "Low": 9800,
  "Close": 10200,
  "Volume": 50000000,
  "MA5": 10100,
  "MA10": 10050,
  "Return": 0.005,
  "Return_1": 0.003,
  "MA_diff": 50
}
```

Response:
```json
{
  "success": true,
  "prediction": {
    "label": 1,
    "label_text": "Naik",
    "probability": 85.5,
    "probability_naik": 85.5,
    "probability_turun": 14.5
  }
}
```

## 📁 Struktur Project

```
SIAB_CBL/
├── siab_project/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── stock_prediction/          # Main application
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── forms.py              # Form definitions
│   ├── ml_model.py           # ML model wrapper
│   ├── admin.py              # Admin configuration
│   ├── urls.py               # URL routing
│   └── templates/            # HTML templates
├── data/                      # Dataset folder
│   └── BBCA.JK_extended.csv
├── siab_model.pkl            # Trained XGBoost model
├── manage.py                 # Django management script
└── requirements.txt          # Python dependencies
```

## 🎓 Model Information

- **Model Type**: XGBoost Classifier
- **Features**: 10 features (Open, High, Low, Close, Volume, MA5, MA10, Return, Return_1, MA_diff)
- **Target**: Binary classification (0=Turun, 1=Naik)
- **Threshold**: 0.3% (0.003)
- **Parameters**:
  - n_estimators: 200
  - max_depth: 6
  - learning_rate: 0.05

## 🔧 Konfigurasi

Edit `siab_project/settings.py` untuk konfigurasi:

- `DEBUG`: Set `False` untuk production
- `ALLOWED_HOSTS`: Tambahkan domain Anda
- `DATABASES`: Ganti ke PostgreSQL/MySQL untuk production
- `MODEL_PATH`: Path ke file model `.pkl`
- `DATA_PATH`: Path ke folder data

## 📊 Admin Panel

Akses admin panel di: **http://localhost:8000/admin**

Login dengan superuser yang telah dibuat untuk:
- Melihat semua prediksi
- Manage stock data
- View statistics

## 🐛 Troubleshooting

### Model tidak bisa di-load
- Pastikan file `siab_model.pkl` ada di root directory
- Pastikan semua dependencies terinstall dengan benar

### Error saat upload CSV
- Pastikan CSV memiliki kolom: Date, Open, High, Low, Close, Volume
- Pastikan format tanggal: YYYY-MM-DD
- File maksimal 10MB

### Chart tidak muncul
- Pastikan koneksi internet aktif (untuk CDN Bootstrap & Chart.js)
- Clear browser cache

## 📝 License

Project ini dibuat untuk keperluan pembelajaran dan penelitian.

## 👨‍💻 Author

Dibuat dengan ❤️ menggunakan Django & XGBoost

---

**Selamat menggunakan SIAB Stock Prediction System!** 🚀
