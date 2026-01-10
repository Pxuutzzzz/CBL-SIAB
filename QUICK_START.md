# 🚀 Cara Menjalankan SIAB Stock Prediction

## ✅ Status: Server Sudah Berjalan!

Django development server sudah aktif di: **http://localhost:8000**

## 📋 Langkah-langkah yang Sudah Dilakukan:

1. ✅ Install semua dependencies (Django, XGBoost, Pandas, dll)
2. ✅ Database migrations sudah dijalankan
3. ✅ Server Django sudah running

## 🌐 Akses Aplikasi:

Buka browser dan kunjungi:
```
http://localhost:8000
```

## 📱 Menu yang Tersedia:

1. **Home** - Dashboard dengan statistik model
2. **Prediksi Manual** - Input data saham manual
3. **Riwayat Prediksi** - Lihat semua prediksi
4. **Visualisasi** - Chart interaktif

## 🛑 Cara Stop Server:

Tekan `Ctrl + C` di terminal

## 🔄 Cara Menjalankan Lagi:

```bash
cd C:\Users\putri\SIAB_CBL
python manage.py runserver
```

## 📝 Catatan Penting:

- Model XGBoost akan di-load otomatis dari `siab_model.pkl`
- Semua prediksi akan tersimpan di database `db.sqlite3`
- Untuk akses admin panel: http://localhost:8000/admin (perlu create superuser dulu)

## 🎯 Quick Start - Test Prediksi:


---

**Server Status**: 🟢 RUNNING
**Port**: 8000
**URL**: http://localhost:8000
