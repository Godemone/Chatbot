#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Chatbot Test Script
Bu dosya chatbot'unuzu kapsamlı bir şekilde test etmenizi sağlar.
"""

from chatbot import SmartChatbot
import time

def test_chatbot_interactive():
    """İnteraktif chatbot testi"""
    print("🤖 Chatbot İnteraktif Test Modu")
    print("=" * 50)
    print("Çıkmak için 'çıkış' yazın")
    print("Test komutları:")
    print("- 'test' : Otomatik test başlatır")
    print("- 'stats' : İstatistikleri gösterir")
    print("- 'save' : Bilgi tabanını kaydeder")
    print("- 'load' : Bilgi tabanını yükler")
    print("=" * 50)
    
    chatbot = SmartChatbot()
    
    while True:
        try:
            user_input = input("\n👤 Siz: ").strip()
            
            if user_input.lower() in ['çıkış', 'exit', 'quit']:
                print("👋 Görüşürüz!")
                break
                
            elif user_input.lower() == 'test':
                run_automated_tests(chatbot)
                continue
                
            elif user_input.lower() == 'stats':
                show_stats(chatbot)
                continue
                
            elif user_input.lower() == 'save':
                chatbot.save_knowledge()
                print("✅ Bilgi tabanı kaydedildi!")
                continue
                
            elif user_input.lower() == 'load':
                chatbot.load_knowledge()
                print("✅ Bilgi tabanı yüklendi!")
                continue
            
            if user_input:
                response = chatbot.chat(user_input)
                print(f"🤖 Bot: {response}")
                
        except KeyboardInterrupt:
            print("\n👋 Görüşürüz!")
            break
        except Exception as e:
            print(f"❌ Hata: {e}")

def run_automated_tests(chatbot):
    """Otomatik testler"""
    print("\n🧪 Otomatik Testler Başlıyor...")
    print("-" * 40)
    
    test_cases = [
        # Selamlaşma testleri
        ("Merhaba!", "greetings"),
        ("Selam!", "greetings"),
        ("Günaydın!", "greetings"),
        ("Hi!", "greetings"),
        
        # Vedalaşma testleri
        ("Güle güle!", "farewells"),
        ("Hoşça kal!", "farewells"),
        ("Görüşürüz!", "farewells"),
        ("Bye!", "farewells"),
        
        # Teşekkür testleri
        ("Teşekkürler!", "thanks"),
        ("Teşekkür ederim!", "thanks"),
        ("Sağol!", "thanks"),
        ("Thanks!", "thanks"),
        
        # Saat testleri
        ("Saat kaç?", "time"),
        ("Zaman nedir?", "time"),
        ("Kaç saat?", "time"),
        
        # Hava durumu testleri
        ("Hava nasıl?", "weather"),
        ("Hava durumu?", "weather"),
        ("Yağmur yağacak mı?", "weather"),
        
        # Matematik testleri
        ("Hesapla 2+2", "math"),
        ("Topla 5 ve 3", "math"),
        ("Matematik işlemi", "math"),
        
        # Bilinmeyen testler
        ("Python nedir?", "unknown"),
        ("Futbol oynuyorum", "unknown"),
        ("Müzik dinliyorum", "unknown"),
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_text, expected_intent) in enumerate(test_cases, 1):
        print(f"\nTest {i}/{total}: '{input_text}'")
        
        # Chatbot'dan yanıt al
        response = chatbot.chat(input_text)
        
        # Niyeti kontrol et
        actual_intent = chatbot.classify_intent(input_text)
        
        if actual_intent == expected_intent:
            print(f"✅ PASS - Niyet: {actual_intent}")
            print(f"   Yanıt: {response}")
            passed += 1
        else:
            print(f"❌ FAIL - Beklenen: {expected_intent}, Gerçek: {actual_intent}")
            print(f"   Yanıt: {response}")
    
    print(f"\n📊 Test Sonuçları: {passed}/{total} başarılı ({passed/total*100:.1f}%)")

def show_stats(chatbot):
    """İstatistikleri göster"""
    stats = chatbot.get_conversation_stats()
    
    print("\n📊 Chatbot İstatistikleri")
    print("-" * 30)
    print(f"Toplam Mesaj: {stats['total_messages']}")
    print(f"Öğrenme Kaydı: {stats['learning_entries']}")
    
    if stats['intents']:
        print("\nNiyet Dağılımı:")
        for intent, count in stats['intents'].items():
            print(f"  {intent}: {count}")

def test_specific_features():
    """Belirli özellikleri test et"""
    print("\n🔧 Özel Özellik Testleri")
    print("-" * 30)
    
    chatbot = SmartChatbot()
    
    # Öğrenme testi
    print("1. Öğrenme Testi:")
    chatbot.learn_from_conversation("Python nedir?", "Python bir programlama dilidir")
    print("   ✅ Öğrenme kaydı eklendi")
    
    # Bilgi kaydetme testi
    print("2. Bilgi Kaydetme Testi:")
    chatbot.save_knowledge()
    print("   ✅ Bilgi tabanı kaydedildi")
    
    # Bilgi yükleme testi
    print("3. Bilgi Yükleme Testi:")
    chatbot.load_knowledge()
    print("   ✅ Bilgi tabanı yüklendi")
    
    print("\n✅ Tüm özel testler tamamlandı!")

def main():
    """Ana test fonksiyonu"""
    print("🤖 Chatbot Test Merkezi")
    print("=" * 50)
    print("1. İnteraktif Test")
    print("2. Otomatik Test")
    print("3. Özel Özellik Testi")
    print("4. Web Arayüzü Testi")
    print("5. Çıkış")
    
    while True:
        try:
            choice = input("\nSeçiminiz (1-5): ").strip()
            
            if choice == "1":
                test_chatbot_interactive()
                break
            elif choice == "2":
                chatbot = SmartChatbot()
                run_automated_tests(chatbot)
                break
            elif choice == "3":
                test_specific_features()
                break
            elif choice == "4":
                print("\n🌐 Web arayüzünü test etmek için:")
                print("1. Terminal'de 'python app.py' komutunu çalıştırın")
                print("2. Tarayıcınızda http://localhost:5000 adresine gidin")
                print("3. Chatbot ile konuşmaya başlayın!")
                break
            elif choice == "5":
                print("👋 Görüşürüz!")
                break
            else:
                print("❌ Geçersiz seçim. Lütfen 1-5 arası bir sayı girin.")
                
        except KeyboardInterrupt:
            print("\n👋 Görüşürüz!")
            break

if __name__ == "__main__":
    main() 