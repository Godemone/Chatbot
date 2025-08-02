# 🤖 Akıllı Chatbot Projesi

Modern ve öğrenme yeteneği olan bir chatbot uygulaması. Bu proje Python, Flask ve NLP teknolojilerini kullanarak geliştirilmiştir.

## ✨ Özellikler

- **Doğal Dil İşleme (NLP)**: NLTK kütüphanesi ile gelişmiş metin analizi
- **Akıllı Niyet Sınıflandırma**: Kullanıcı mesajlarını otomatik olarak kategorize eder
- **Öğrenme Yeteneği**: Konuşma geçmişinden öğrenir ve gelişir
- **Modern Web Arayüzü**: Responsive tasarım ile güzel kullanıcı deneyimi
- **Gerçek Zamanlı İstatistikler**: Konuşma analizi ve performans metrikleri
- **Bilgi Tabanı Yönetimi**: Öğrenilen bilgileri kaydetme ve yükleme

## 🚀 Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

### Adım 1: Projeyi İndirin
```bash
git clone <repository-url>
cd chatbot-project
```

### Adım 2: Sanal Ortam Oluşturun (Önerilen)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Adım 3: Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### Adım 4: NLTK Verilerini İndirin
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

## 🎯 Kullanım

### Web Uygulamasını Başlatın
```bash
python app.py
```

Tarayıcınızda `http://localhost:5000` adresine gidin.

### Terminal Testi
```bash
python chatbot.py
```

## 📋 Özellikler Detayı

### 🤖 Chatbot Yetenekleri

1. **Selamlaşma ve Vedalaşma**
   - "Merhaba", "Selam", "Güle güle" gibi temel selamlaşmalar

2. **Saat ve Tarih Bilgisi**
   - "Saat kaç?" sorusuna gerçek zamanlı yanıt
   - Güncel tarih bilgisi

3. **Hava Durumu Konuşması**
   - Hava durumu hakkında konuşma başlatma
   - Şehir bazlı hava durumu sorgulama

4. **Matematik İşlemleri**
   - Temel matematik işlemleri için hazırlık
   - Hesaplama isteklerini algılama

5. **Sürekli Öğrenme**
   - Kullanıcı geri bildirimlerinden öğrenme
   - Konuşma geçmişini analiz etme

### 🎨 Web Arayüzü

- **Modern Tasarım**: Gradient renkler ve yumuşak animasyonlar
- **Responsive**: Mobil ve masaüstü uyumlu
- **Gerçek Zamanlı**: Typing indicator ve anlık mesajlaşma
- **İstatistikler**: Konuşma analizi ve performans metrikleri

### 📊 İstatistikler

- Toplam mesaj sayısı
- Niyet dağılımı (greetings, weather, time, vb.)
- Öğrenme kayıt sayısı
- Konuşma geçmişi

## 🔧 API Endpoints

### POST `/chat`
Chatbot ile konuşma başlatın.

**Request:**
```json
{
    "message": "Merhaba!"
}
```

**Response:**
```json
{
    "response": "Merhaba! Size nasıl yardımcı olabilirim?",
    "stats": {
        "total_messages": 1,
        "intents": {"greetings": 1},
        "learning_entries": 0
    },
    "timestamp": "2024-01-01T12:00:00"
}
```

### GET `/stats`
Konuşma istatistiklerini alın.

### POST `/save`
Bilgi tabanını kaydedin.

### POST `/load`
Bilgi tabanını yükleyin.

### POST `/learn`
Öğrenme verisi ekleyin.

## 🛠️ Geliştirme

### Proje Yapısı
```
chatbot-project/
├── app.py                 # Flask web uygulaması
├── chatbot.py            # Ana chatbot sınıfı
├── requirements.txt      # Python bağımlılıkları
├── templates/
│   └── index.html       # Web arayüzü
└── README.md            # Bu dosya
```

### Yeni Özellik Ekleme

1. **Yeni Niyet Ekleme**: `classify_intent()` metoduna yeni kelime grupları ekleyin
2. **Yeni Yanıt Ekleme**: `knowledge_base` sözlüğüne yeni kategoriler ekleyin
3. **Yeni API Endpoint**: `app.py` dosyasına yeni route'lar ekleyin

### Test Etme
```bash
# Unit testler
python -m pytest tests/

# Manuel test
python chatbot.py
```

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🙏 Teşekkürler

- NLTK kütüphanesi için
- Flask framework'ü için
- Scikit-learn kütüphanesi için

## 📞 İletişim

Sorularınız için issue açabilir veya pull request gönderebilirsiniz.

---

**Not**: Bu chatbot eğitim amaçlı geliştirilmiştir. Gerçek dünya uygulamaları için daha gelişmiş NLP modelleri kullanmanız önerilir. 