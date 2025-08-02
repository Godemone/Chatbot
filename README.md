# 🤖 Akıllı Chatbot

Bu proje, Python ile geliştirilmiş akıllı bir chatbot uygulamasıdır. Chatbot, doğal dil işleme teknikleri kullanarak kullanıcılarla etkileşim kurar ve sürekli öğrenme yeteneğine sahiptir.

## ✨ Özellikler

### 🧠 Temel Özellikler
- **Doğal Dil İşleme**: NLTK kütüphanesi ile gelişmiş metin analizi
- **Akıllı Yanıt Sistemi**: Kullanıcı niyetini anlayarak uygun yanıtlar üretme
- **Sürekli Öğrenme**: Kullanıcı etkileşimlerinden öğrenme
- **Web Arayüzü**: Modern ve kullanıcı dostu web arayüzü

### 🎯 Desteklenen Kategoriler
- **Selamlaşma**: Merhaba, selam, hey vb.
- **Vedalaşma**: Güle güle, hoşça kal vb.
- **Teşekkür**: Teşekkürler, sağol vb.
- **Saat ve Tarih**: Güncel saat ve tarih bilgisi
- **Matematik İşlemleri**: Toplama, çıkarma, çarpma, bölme
- **Fıkralar**: Programlama ve teknoloji temalı fıkralar
- **İlginç Bilgiler**: Teknoloji ve bilim hakkında ilginç bilgiler
- **Yardım**: Bot'un yapabileceklerini açıklama

### 📚 Öğrenme Özellikleri
- **Yeni Yanıt Öğretme**: Web arayüzünden bot'a yeni yanıtlar öğretme
- **Özel Tetikleyiciler**: Belirli kelimeler için özel yanıtlar tanımlama
- **Bilgi Kaydetme**: Öğrenilen bilgileri JSON formatında kaydetme
- **Bilgi Yükleme**: Kaydedilen bilgileri geri yükleme

### 🛑 Kapatma Özellikleri
- **Otomatik Kapatma**: Python scriptleri ile güvenli kapatma
- **Port Kontrolü**: Port 5000'in serbest kalmasını sağlama
- **RAM Temizliği**: Python işlemlerinin tamamen sonlandırılması
- **Çoklu Yöntem**: Script, batch dosyası ve manuel kapatma seçenekleri

## 🚀 Kurulum

### Gereksinimler
- Python 3.7+
- Flask
- NLTK
- Flask-CORS

### Kurulum Adımları

1. **Projeyi klonlayın:**
```bash
git clone <repository-url>
cd Chatbot
```

2. **Gerekli paketleri yükleyin:**
```bash
pip install -r requirements.txt
```

3. **NLTK verilerini indirin:**
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

## 🎮 Kullanım

### Web Arayüzü ile Kullanım

1. **Sunucuyu başlatın:**
```bash
python app.py
```

2. **Tarayıcınızda açın:**
```
http://localhost:5000
```

3. **Chatbot ile konuşmaya başlayın!**

### Chatbot'u Kapatma

#### Basit Kapatma:
```bash
python stop_simple.py
```

#### Gelişmiş Kapatma (psutil gerekli):
```bash
pip install psutil
python stop_chatbot.py
```

#### Windows Batch Dosyası:
```bash
stop_chatbot.bat
```

#### Manuel Kapatma:
- **Terminal'de:** `Ctrl + C`
- **Task Manager:** Python işlemlerini sonlandır
- **Komut:** `taskkill /f /im python3.13.exe`

### Bot'a Yeni Şeyler Öğretme

1. **Web arayüzünde 📚 butonuna tıklayın**
2. **Tetikleyici kelime/cümle girin** (örn: "python")
3. **Bot'un vereceği yanıtı yazın** (örn: "Python harika bir programlama dilidir!")
4. **"Öğret" butonuna tıklayın**

### Komut Satırı ile Kullanım

```python
from chatbot import SmartChatbot

# Chatbot oluştur
chatbot = SmartChatbot()

# Konuşma
response = chatbot.chat("Merhaba!")
print(response)

# Yeni yanıt öğret
chatbot.teach_new_response("python", "Python harika bir programlama dilidir!")

# Matematik işlemi
response = chatbot.chat("5 ve 3 topla")
print(response)  # "5 + 3 = 8"

# Bilgi kaydet
chatbot.save_knowledge()

# Bilgi yükle
chatbot.load_knowledge()
```

## 🧪 Test

### Otomatik Testler
```bash
python test_chatbot.py
```

### Manuel Testler
```bash
python chatbot.py
```

## 📊 API Endpoints

### POST /chat
Chatbot ile konuşma
```json
{
  "message": "Merhaba!"
}
```

### POST /teach
Bot'a yeni yanıt öğretme
```json
{
  "trigger": "python",
  "response": "Python harika bir programlama dilidir!"
}
```

### GET /stats
Konuşma istatistiklerini alma

### POST /save
Bilgi tabanını kaydetme

### POST /load
Bilgi tabanını yükleme

### GET /custom_responses
Özel öğrenilen yanıtları alma

## 🏗️ Proje Yapısı

```
Chatbot/
├── app.py                 # Flask web uygulaması
├── chatbot.py            # Ana chatbot sınıfı
├── test_chatbot.py       # Test dosyası
├── stop_simple.py        # Basit kapatma scripti
├── stop_chatbot.py       # Gelişmiş kapatma scripti
├── stop_chatbot.bat      # Windows batch dosyası
├── requirements.txt       # Python bağımlılıkları
├── README.md             # Bu dosya
└── templates/
    └── index.html        # Web arayüzü
```

## 🔧 Özelleştirme

### Yeni Kategoriler Ekleme

`chatbot.py` dosyasında `knowledge_base` sözlüğüne yeni kategoriler ekleyebilirsiniz:

```python
self.knowledge_base["yeni_kategori"] = [
    "Yanıt 1",
    "Yanıt 2",
    "Yanıt 3"
]
```

### Yeni Niyet Tanımlama

`classify_intent` fonksiyonuna yeni niyet tanımları ekleyebilirsiniz:

```python
# Yeni niyet
new_words = ['yeni', 'kelime', 'grubu']
if any(word in text for word in new_words):
    return "yeni_niyet"
```

### Yeni Yanıt Fonksiyonu

`get_response` fonksiyonuna yeni yanıt mantığı ekleyebilirsiniz:

```python
elif intent == "yeni_niyet":
    return "Yeni yanıt mantığı"
```

## 📈 İstatistikler

Chatbot şu istatistikleri tutar:
- **Toplam Mesaj Sayısı**: Kaç mesaj alındığı
- **Niyet Dağılımı**: Hangi kategorilerde kaç mesaj var
- **Öğrenme Kayıtları**: Kaç yeni şey öğretildiği

## 🤝 Katkıda Bulunma

1. Projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🆘 Destek

Herhangi bir sorun yaşarsanız:
1. GitHub Issues bölümünde sorun bildirin
2. Detaylı hata mesajları ile birlikte açıklama yapın
3. Hangi adımları takip ettiğinizi belirtin

## 🎯 Gelecek Planları

- [ ] Çoklu dil desteği
- [ ] Ses tanıma ve sentezleme
- [ ] Görsel işleme yetenekleri
- [ ] Makine öğrenmesi entegrasyonu
- [ ] Mobil uygulama
- [ ] API dokümantasyonu
- [ ] Daha gelişmiş doğal dil işleme

---

**Not**: Bu chatbot eğitim amaçlı geliştirilmiştir ve sürekli geliştirilmektedir. Gerçek dünya uygulamaları için daha gelişmiş NLP kütüphaneleri kullanmanız önerilir. 