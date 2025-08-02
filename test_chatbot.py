#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Chatbot Test Script
Bu dosya chatbot'unuzu kapsamlı bir şekilde test etmenizi sağlar.
"""

import unittest
from chatbot import SmartChatbot
from datetime import datetime

class TestSmartChatbot(unittest.TestCase):
    
    def setUp(self):
        """Her test öncesi yeni chatbot oluştur"""
        self.chatbot = SmartChatbot()
    
    def test_greetings(self):
        """Selamlaşma testleri"""
        responses = []
        greetings = ["merhaba", "selam", "hey", "hi", "hello"]
        
        for greeting in greetings:
            response = self.chatbot.chat(greeting)
            responses.append(response)
            self.assertIsNotNone(response)
            self.assertGreater(len(response), 0)
        
        # En az bir farklı yanıt olmalı
        self.assertGreater(len(set(responses)), 1)
    
    def test_farewells(self):
        """Vedalaşma testleri"""
        response = self.chatbot.chat("güle güle")
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)
    
    def test_thanks(self):
        """Teşekkür testleri"""
        response = self.chatbot.chat("teşekkürler")
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)
    
    def test_time(self):
        """Saat testi"""
        response = self.chatbot.chat("saat kaç")
        self.assertIsNotNone(response)
        self.assertIn(":", response)  # Saat formatı içermeli
    
    def test_math_operations(self):
        """Matematik işlemleri testleri"""
        # Toplama
        response = self.chatbot.chat("5 ve 3 topla")
        self.assertIn("5 + 3 = 8", response)
        
        # Çıkarma
        response = self.chatbot.chat("10 çıkar 4")
        self.assertIn("10 - 4 = 6", response)
        
        # Çarpma
        response = self.chatbot.chat("6 çarp 7")
        self.assertIn("6 × 7 = 42", response)
        
        # Bölme
        response = self.chatbot.chat("15 böl 3")
        self.assertIn("15 ÷ 3 = 5.0", response)
    
    def test_jokes(self):
        """Fıkra testleri"""
        response = self.chatbot.chat("fıkra anlat")
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)
    
    def test_facts(self):
        """İlginç bilgi testleri"""
        response = self.chatbot.chat("ilginç bilgi ver")
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)
    
    def test_help(self):
        """Yardım testi"""
        response = self.chatbot.chat("yardım")
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)
    
    def test_teaching(self):
        """Öğretme testi"""
        # Yeni yanıt öğret
        self.chatbot.teach_new_response("test", "Bu bir test yanıtıdır!")
        
        # Öğretilen yanıtı test et
        response = self.chatbot.chat("test")
        self.assertEqual(response, "Bu bir test yanıtıdır!")
    
    def test_custom_responses(self):
        """Özel yanıtlar testi"""
        # Özel yanıt ekle
        self.chatbot.custom_responses["özel"] = "Bu özel bir yanıttır!"
        
        # Test et
        response = self.chatbot.chat("özel")
        self.assertEqual(response, "Bu özel bir yanıttır!")
    
    def test_conversation_history(self):
        """Konuşma geçmişi testi"""
        self.chatbot.chat("merhaba")
        self.chatbot.chat("nasılsın")
        
        history = self.chatbot.conversation_history
        self.assertEqual(len(history), 2)
        self.assertIn('user', history[0])
        self.assertIn('bot', history[0])
        self.assertIn('timestamp', history[0])
    
    def test_learning_history(self):
        """Öğrenme geçmişi testi"""
        self.chatbot.learn_from_conversation("test input", "test feedback")
        
        learning_history = self.chatbot.learning_history
        self.assertEqual(len(learning_history), 1)
        self.assertEqual(learning_history[0]['input'], "test input")
        self.assertEqual(learning_history[0]['feedback'], "test feedback")
    
    def test_stats(self):
        """İstatistik testi"""
        self.chatbot.chat("merhaba")
        self.chatbot.chat("güle güle")
        
        stats = self.chatbot.get_conversation_stats()
        self.assertEqual(stats['total_messages'], 2)
        self.assertIn('greetings', stats['intents'])
        self.assertIn('farewells', stats['intents'])
    
    def test_save_load_knowledge(self):
        """Kaydetme ve yükleme testi"""
        # Özel yanıt ekle
        self.chatbot.teach_new_response("test_save", "Test yanıtı")
        
        # Kaydet
        self.chatbot.save_knowledge("test_knowledge.json")
        
        # Yeni chatbot oluştur ve yükle
        new_chatbot = SmartChatbot()
        new_chatbot.load_knowledge("test_knowledge.json")
        
        # Test et
        response = new_chatbot.chat("test_save")
        self.assertEqual(response, "Test yanıtı")
        
        # Test dosyasını temizle
        import os
        if os.path.exists("test_knowledge.json"):
            os.remove("test_knowledge.json")
    
    def test_unknown_intent(self):
        """Bilinmeyen niyet testi"""
        response = self.chatbot.chat("xyzabc123")
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)
    
    def test_text_preprocessing(self):
        """Metin ön işleme testi"""
        processed = self.chatbot.preprocess_text("Merhaba Dünya!")
        self.assertIsInstance(processed, str)
        self.assertGreater(len(processed), 0)

def run_interactive_test():
    """İnteraktif test fonksiyonu"""
    print("🤖 Chatbot İnteraktif Test Başlıyor...\n")
    
    chatbot = SmartChatbot()
    
    # Örnek kullanım
    test_cases = [
        ("Merhaba!", "Selamlaşma"),
        ("Fıkra anlat", "Fıkra"),
        ("İlginç bilgi ver", "İlginç bilgi"),
        ("5 ve 3 topla", "Matematik"),
        ("Saat kaç?", "Saat"),
        ("Yardım", "Yardım"),
        ("Güle güle", "Vedalaşma")
    ]
    
    for user_input, description in test_cases:
        print(f"🧪 Test: {description}")
        print(f"👤 Kullanıcı: {user_input}")
        response = chatbot.chat(user_input)
        print(f"🤖 Bot: {response}")
        print("-" * 50)
    
    # Öğretme testi
    print("📚 Öğretme Testi:")
    chatbot.teach_new_response("python", "Python harika bir programlama dilidir!")
    response = chatbot.chat("python")
    print(f"👤 Kullanıcı: python")
    print(f"🤖 Bot: {response}")
    print("-" * 50)
    
    # İstatistikler
    stats = chatbot.get_conversation_stats()
    print("📊 Test İstatistikleri:")
    print(f"Toplam mesaj: {stats['total_messages']}")
    print(f"Öğrenme kayıtları: {stats['learning_entries']}")
    print(f"Niyet dağılımı: {stats['intents']}")

if __name__ == '__main__':
    # Unit testleri çalıştır
    print("🧪 Unit Testler Başlıyor...")
    unittest.main(verbosity=2, exit=False)
    
    print("\n" + "="*60 + "\n")
    
    # İnteraktif test çalıştır
    run_interactive_test() 