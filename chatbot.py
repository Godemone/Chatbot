import json
import random
import re
from datetime import datetime
from typing import Dict, List, Tuple
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# Basit matematik işlemleri için hazırlık

# NLTK verilerini indir
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

class SmartChatbot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('turkish'))
        # Basit metin işleme için hazırlık
        
        # Temel bilgi tabanı
        self.knowledge_base = {
            "greetings": [
                "Merhaba! Size nasıl yardımcı olabilirim?",
                "Selam! Bugün nasılsınız?",
                "Hoş geldiniz! Ne konuda yardıma ihtiyacınız var?",
                "Merhaba! Ben size nasıl yardımcı olabilirim?"
            ],
            "farewells": [
                "Görüşmek üzere! İyi günler!",
                "Hoşça kalın! Tekrar görüşmek üzere!",
                "İyi günler! Başka bir sorunuz olursa buradayım!",
                "Güle güle! Yine bekleriz!"
            ],
            "thanks": [
                "Rica ederim! Başka bir konuda yardıma ihtiyacınız var mı?",
                "Ne demek! Size yardımcı olabildiysem ne mutlu bana!",
                "Çok rica ederim! Başka bir sorunuz olursa sormaktan çekinmeyin!",
                "Ben teşekkür ederim! İyi günler!"
            ],
            "unknown": [
                "Bu konuda henüz bilgim yok, ama öğrenmeye çalışıyorum!",
                "Üzgünüm, bu konuda size yardımcı olamıyorum. Başka bir şey sorabilir misiniz?",
                "Bu konu hakkında bilgim yok, ama sürekli öğreniyorum!",
                "Henüz bu konuda eğitilmedim. Başka nasıl yardımcı olabilirim?"
            ],
            # Yeni kategoriler
            "jokes": [
                "Programcı neden karanlıkta çalışır? Çünkü ışık bug'ları çeker! 😄",
                "İki programcı markete gider. Birisi 'Süt al' der, diğeri 'Süt yoksa yoğurt al' der! 😂",
                "Neden bilgisayarlar soğuktan korkar? Çünkü Windows'ları kapatırlar! 🪟",
                "Bir programcı karısına 'Marketten ekmek al' der. Karısı 'Ekmek yoksa ne alayım?' der. Programcı 'Hiçbir şey alma' der! 🥖"
            ],
            "facts": [
                "İlk bilgisayar programcısı Ada Lovelace'tı ve 1843'te ilk algoritma yazdı!",
                "Python programlama dili adını Monty Python komedi grubundan almıştır!",
                "İnternet'in %60'ı kedi videolarından oluşur (şaka değil!) 😸",
                "Bir bilgisayar saniyede 1 milyar işlem yapabilir!"
            ],
            "help": [
                "Size nasıl yardımcı olabilirim? Şunları yapabilirim:\n- Selamlaşma\n- Fıkra anlatma\n- İlginç bilgiler\n- Saat söyleme\n- Matematik işlemleri",
                "Yardım için şunları deneyebilirsiniz:\n- 'Fıkra anlat'\n- 'İlginç bilgi ver'\n- 'Saat kaç?'\n- 'Hesapla 2+2'",
                "Komutlarım:\n- Selamlaşma\n- Fıkra\n- Bilgi\n- Saat\n- Hesaplama"
            ]
        }
        
        # Öğrenme geçmişi
        self.learning_history = []
        
        # Kullanıcı tercihleri
        self.user_preferences = {}
        
        # Konuşma geçmişi
        self.conversation_history = []
        
        # Yeni öğrenilen bilgiler
        self.custom_responses = {}
        
        # Matematik işlemleri için hazırlık
        self.math_operations = {
            'topla': lambda x, y: x + y,
            'çıkar': lambda x, y: x - y,
            'çarp': lambda x, y: x * y,
            'böl': lambda x, y: x / y if y != 0 else "Sıfıra bölme hatası!"
        }
    
    def preprocess_text(self, text: str) -> str:
        """Metni ön işleme"""
        # Küçük harfe çevir
        text = text.lower()
        
        # Özel karakterleri temizle
        text = re.sub(r'[^\w\s]', '', text)
        
        # Tokenize et
        tokens = word_tokenize(text)
        
        # Stop words'leri kaldır ve lemmatize et
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token not in self.stop_words and len(token) > 2]
        
        return ' '.join(tokens)
    
    def classify_intent(self, text: str) -> str:
        """Kullanıcı niyetini sınıflandır"""
        text = text.lower()
        
        # Selamlaşma
        greeting_words = ['merhaba', 'selam', 'hey', 'hi', 'hello', 'günaydın', 'iyi günler']
        if any(word in text for word in greeting_words):
            return "greetings"
        
        # Vedalaşma
        farewell_words = ['güle güle', 'hoşça kal', 'görüşürüz', 'bye', 'goodbye', 'çıkış']
        if any(word in text for word in farewell_words):
            return "farewells"
        
        # Teşekkür
        thanks_words = ['teşekkür', 'teşekkürler', 'sağol', 'thanks', 'thank you', 'teşekkür ederim']
        if any(word in text for word in thanks_words):
            return "thanks"
        
        # Hava durumu
        weather_words = ['hava', 'durum', 'yağmur', 'güneş', 'sıcak', 'soğuk', 'weather']
        if any(word in text for word in weather_words):
            return "weather"
        
        # Saat
        time_words = ['saat', 'kaç', 'zaman', 'time', 'saati']
        if any(word in text for word in time_words):
            return "time"
        
        # Matematik
        math_words = ['hesapla', 'topla', 'çıkar', 'çarp', 'böl', 'matematik', 'hesap']
        if any(word in text for word in math_words):
            return "math"
        
        # Fıkra
        joke_words = ['fıkra', 'şaka', 'espri', 'güldür', 'komik', 'joke', 'funny']
        if any(word in text for word in joke_words):
            return "jokes"
        
        # İlginç bilgiler
        fact_words = ['bilgi', 'ilginç', 'fact', 'öğren', 'öğret', 'söyle']
        if any(word in text for word in fact_words):
            return "facts"
        
        # Yardım
        help_words = ['yardım', 'help', 'ne yapabilirsin', 'komutlar', 'özellikler']
        if any(word in text for word in help_words):
            return "help"
        
        # Özel öğrenilen yanıtları kontrol et
        for key in self.custom_responses:
            if key.lower() in text:
                return "custom"
        
        return "unknown"
    
    def get_response(self, intent: str, user_input: str = "") -> str:
        """Niyete göre yanıt üret"""
        if intent == "greetings":
            return random.choice(self.knowledge_base["greetings"])
        
        elif intent == "farewells":
            return random.choice(self.knowledge_base["farewells"])
        
        elif intent == "thanks":
            return random.choice(self.knowledge_base["thanks"])
        
        elif intent == "weather":
            return "Hava durumu bilgisi için size yardımcı olabilirim! Hangi şehir için bilgi istiyorsunuz?"
        
        elif intent == "time":
            current_time = datetime.now().strftime("%H:%M:%S")
            current_date = datetime.now().strftime("%d/%m/%Y")
            return f"Şu anki saat: {current_time}\nTarih: {current_date}"
        
        elif intent == "math":
            return self.handle_math_operation(user_input)
        
        elif intent == "jokes":
            return random.choice(self.knowledge_base["jokes"])
        
        elif intent == "facts":
            return random.choice(self.knowledge_base["facts"])
        
        elif intent == "help":
            return random.choice(self.knowledge_base["help"])
        
        elif intent == "custom":
            return self.get_custom_response(user_input)
        
        else:
            return random.choice(self.knowledge_base["unknown"])
    
    def learn_from_conversation(self, user_input: str, user_feedback: str = None):
        """Konuşmadan öğren"""
        if user_feedback:
            self.learning_history.append({
                'input': user_input,
                'feedback': user_feedback,
                'timestamp': datetime.now().isoformat()
            })
    
    def teach_new_response(self, trigger: str, response: str):
        """Yeni yanıt öğret"""
        self.custom_responses[trigger.lower()] = response
        self.learning_history.append({
            'input': f"Öğretme: {trigger}",
            'feedback': f"Yeni yanıt: {response}",
            'timestamp': datetime.now().isoformat()
        })
    
    def get_custom_response(self, user_input: str) -> str:
        """Özel öğrenilen yanıtları döndür"""
        for trigger, response in self.custom_responses.items():
            if trigger in user_input.lower():
                return response
        return "Bu konuda henüz bir şey öğrenmedim."
    
    def handle_math_operation(self, user_input: str) -> str:
        """Matematik işlemlerini yap"""
        try:
            # Sayıları ve operatörleri bul
            import re
            numbers = re.findall(r'\d+', user_input)
            if len(numbers) >= 2:
                num1, num2 = int(numbers[0]), int(numbers[1])
                
                # Operatörü bul
                if any(op in user_input for op in ['topla', '+', 'plus']):
                    result = self.math_operations['topla'](num1, num2)
                    return f"{num1} + {num2} = {result}"
                elif any(op in user_input for op in ['çıkar', '-', 'minus']):
                    result = self.math_operations['çıkar'](num1, num2)
                    return f"{num1} - {num2} = {result}"
                elif any(op in user_input for op in ['çarp', '*', 'multiply']):
                    result = self.math_operations['çarp'](num1, num2)
                    return f"{num1} × {num2} = {result}"
                elif any(op in user_input for op in ['böl', '/', 'divide']):
                    result = self.math_operations['böl'](num1, num2)
                    if isinstance(result, str):
                        return result
                    return f"{num1} ÷ {num2} = {result}"
                else:
                    return f"Sayılar: {num1}, {num2}. Hangi işlemi yapmak istiyorsunuz? (topla, çıkar, çarp, böl)"
            else:
                return "Matematik işlemi için en az 2 sayı gerekli. Örnek: '5 ve 3 topla'"
        except Exception as e:
            return f"Matematik işlemi yapılırken hata oluştu: {str(e)}"
    
    def chat(self, user_input: str) -> str:
        """Ana sohbet fonksiyonu"""
        # Konuşma geçmişine ekle
        self.conversation_history.append({
            'user': user_input,
            'timestamp': datetime.now().isoformat()
        })
        
        # Niyeti sınıflandır
        intent = self.classify_intent(user_input)
        
        # Yanıt üret
        response = self.get_response(intent, user_input)
        
        # Yanıtı geçmişe ekle
        self.conversation_history[-1]['bot'] = response
        self.conversation_history[-1]['intent'] = intent
        
        return response
    
    def get_conversation_stats(self) -> Dict:
        """Konuşma istatistiklerini döndür"""
        if not self.conversation_history:
            return {"total_messages": 0, "intents": {}}
        
        intents = {}
        for msg in self.conversation_history:
            if 'intent' in msg:
                intent = msg['intent']
                intents[intent] = intents.get(intent, 0) + 1
        
        return {
            "total_messages": len(self.conversation_history),
            "intents": intents,
            "learning_entries": len(self.learning_history)
        }
    
    def save_knowledge(self, filename: str = "chatbot_knowledge.json"):
        """Bilgi tabanını kaydet"""
        data = {
            "knowledge_base": self.knowledge_base,
            "learning_history": self.learning_history,
            "user_preferences": self.user_preferences,
            "conversation_history": self.conversation_history,
            "custom_responses": self.custom_responses
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_knowledge(self, filename: str = "chatbot_knowledge.json"):
        """Bilgi tabanını yükle"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            self.knowledge_base = data.get("knowledge_base", self.knowledge_base)
            self.learning_history = data.get("learning_history", [])
            self.user_preferences = data.get("user_preferences", {})
            self.conversation_history = data.get("conversation_history", [])
            self.custom_responses = data.get("custom_responses", {})
            
        except FileNotFoundError:
            print("Bilgi dosyası bulunamadı. Yeni bir tane oluşturulacak.")

# Test fonksiyonu
def test_chatbot():
    """Chatbot'u test et"""
    chatbot = SmartChatbot()
    
    test_inputs = [
        "Merhaba!",
        "Nasılsın?",
        "Saat kaç?",
        "Hava nasıl?",
        "Teşekkürler!",
        "Güle güle!"
    ]
    
    print("🤖 Chatbot Test Başlıyor...\n")
    
    for user_input in test_inputs:
        print(f"👤 Kullanıcı: {user_input}")
        response = chatbot.chat(user_input)
        print(f"🤖 Bot: {response}\n")
    
    # İstatistikleri göster
    stats = chatbot.get_conversation_stats()
    print("📊 Konuşma İstatistikleri:")
    print(f"Toplam mesaj: {stats['total_messages']}")
    print(f"Öğrenme kayıtları: {stats['learning_entries']}")
    print(f"Niyet dağılımı: {stats['intents']}")

if __name__ == "__main__":
    test_chatbot() 