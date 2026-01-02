# SIAB Stock Prediction System

Sistem prediksi saham BBCA menggunakan XGBoost Machine Learning yang terintegrasi dengan Django Web Framework.

## 📋 Deskripsi

Aplikasi web ini menggunakan model XGBoost yang telah ditraining untuk memprediksi pergerakan harga saham BBCA (Bank Central Asia). Model dapat memprediksi apakah harga saham akan **Naik** atau **Turun** berdasarkan data historis dan technical indicators.

## ✨ Fitur

- 🎯 **Prediksi Manual**: Input data saham secara manual untuk prediksi real-time
- 📊 **Batch Prediction**: Upload file CSV untuk prediksi multiple data sekaligus
- 📈 **Visualisasi Interaktif**: Chart dan grafik untuk analisis data
- 📝 **Riwayat Prediksi**: Simpan dan lihat semua prediksi yang pernah dibuat
- 🔌 **REST API**: Endpoint API untuk integrasi dengan sistem lain
- 💾 **Database Storage**: Semua prediksi tersimpan di database

## 🛠️ Teknologi

- **Backend**: Django 5.0.1
- **Machine Learning**: XGBoost 3.1.2, scikit-learn 1.6.1
- **Data Processing**: Pandas 2.2.0, NumPy 2.3.5
- **Visualization**: Chart.js, Plotly 5.24.1
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (default)

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
