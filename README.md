# SMS Spam Detection

Türkçe SMS mesajlarını spam olup olmadığını tespit eden web uygulaması. TensorFlow ve FastAPI kullanılarak geliştirilmiştir.

## 🚀 Özellikler

- **Akıllı Spam Tespiti**: Makine öğrenmesi ile SMS mesajlarını analiz eder
- **Modern Arayüz**: Responsive ve kullanıcı dostu web arayüzü
- **Gerçek Zamanlı Tahmin**: Anında sonuç alabilirsiniz
- **Geçmiş Kayıtları**: Son tahminleri görüntüleyebilirsiniz
- **Türkçe Destek**: Türkçe SMS mesajları için optimize edilmiştir

## 🛠️ Teknolojiler

- **Backend**: FastAPI, Python
- **Frontend**: HTML, CSS, JavaScript
- **ML Model**: TensorFlow/Keras
- **Text Processing**: Tokenization, Sequence Padding

## 📦 Kurulum

### Gereksinimler
- Python 3.11+
- pip

### Adımlar

1. **Repository'yi klonlayın**
```bash
git clone https://github.com/musa-arrow/SMS_Project.git
cd SMS_Project
```

2. **Sanal ortam oluşturun**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

4. **Uygulamayı çalıştırın**
```bash
uvicorn app:app --reload
```

5. **Tarayıcıda açın**
```
http://localhost:8000
```

## 🎯 Kullanım

1. Ana sayfada SMS mesajınızı yazın
2. "Tahmin Et" butonuna tıklayın
3. Sonucu görün: **Spam** veya **Spam Değil**
4. Geçmiş tahminlerinizi kontrol edin

### Örnek Mesajlar

**Spam Örneği:**
```
Bahiscom'dan 9 - 10 Ekim size ozel! SUPER CEVRIMSIZ %99 5000TL Nakit Bonus! Tum alanlarda gecerli! https://cutt.ly/bahistenhediye
```

**Normal Mesaj Örneği:**
```
Merhaba, yarın saat 14:00'te buluşalım mı? Teşekkürler.
```

## 📁 Proje Yapısı

```
SMS_Project/
├── app.py              # FastAPI uygulaması
├── requirements.txt    # Python bağımlılıkları
├── sms.h5             # Eğitilmiş model
├── tokenizer.pkl      # Metin tokenizer'ı
├── templates/
│   └── index.html     # Web arayüzü
└── README.md          # Bu dosya
```

## 🔧 API Endpoints

### GET /
Ana sayfa - Web arayüzü

### POST /predict
SMS mesajını analiz eder

**Request:**
```json
{
  "Message": "SMS mesajınız buraya"
}
```

**Response:**
```json
{
  "predicted": 1  // 1: Spam, 0: Spam Değil
}
```

## 🚀 Deployment

### Render (Önerilen)
1. GitHub repository'yi Render'a bağlayın
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

### Railway
1. Railway'e GitHub repository'yi bağlayın
2. Otomatik olarak Python uygulaması olarak algılanır
3. Deploy edin

### VPS/Dedicated Server
```bash
# Nginx + Gunicorn ile
pip install gunicorn
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 📊 Model Performansı

- **Doğruluk**: %99+
- **Desteklenen Dil**: Türkçe
- **Maksimum Mesaj Uzunluğu**: 500 karakter
- **Model Boyutu**: ~50MB

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 👨‍💻 Geliştirici

**Musa Arrow**
- GitHub: [@musa-arrow](https://github.com/musa-arrow)

## 🙏 Teşekkürler

- TensorFlow ekibine
- FastAPI geliştiricilerine
- Açık kaynak topluluğuna

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

