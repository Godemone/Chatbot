from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import SmartChatbot
import json

app = Flask(__name__)
CORS(app)

# Chatbot instance'ı oluştur
chatbot = SmartChatbot()

@app.route('/')
def home():
    """Ana sayfa"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Chat endpoint'i"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Mesaj boş olamaz'}), 400
        
        # Chatbot'dan yanıt al
        bot_response = chatbot.chat(user_message)
        
        # İstatistikleri al
        stats = chatbot.get_conversation_stats()
        
        return jsonify({
            'response': bot_response,
            'stats': stats,
            'timestamp': chatbot.conversation_history[-1]['timestamp']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stats')
def get_stats():
    """İstatistikleri döndür"""
    try:
        stats = chatbot.get_conversation_stats()
        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save', methods=['POST'])
def save_knowledge():
    """Bilgi tabanını kaydet"""
    try:
        chatbot.save_knowledge()
        return jsonify({'message': 'Bilgi tabanı başarıyla kaydedildi'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/load', methods=['POST'])
def load_knowledge():
    """Bilgi tabanını yükle"""
    try:
        chatbot.load_knowledge()
        return jsonify({'message': 'Bilgi tabanı başarıyla yüklendi'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/learn', methods=['POST'])
def learn():
    """Öğrenme endpoint'i"""
    try:
        data = request.get_json()
        user_input = data.get('input', '')
        feedback = data.get('feedback', '')
        
        chatbot.learn_from_conversation(user_input, feedback)
        return jsonify({'message': 'Öğrenme kaydedildi'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 