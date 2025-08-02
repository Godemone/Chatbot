#!/usr/bin/env python3
"""
Basit Chatbot Kapatma Scripti
"""

import subprocess
import time

def stop_chatbot():
    """Chatbot'u kapat"""
    print("🛑 Chatbot kapatılıyor...")
    
    # Python işlemlerini bul ve kapat
    commands = [
        ['taskkill', '/f', '/im', 'python3.13.exe'],
        ['taskkill', '/f', '/im', 'python.exe'],
        ['taskkill', '/f', '/im', 'python3.exe']
    ]
    
    for cmd in commands:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ {cmd[2]} işlemleri kapatıldı.")
            else:
                print(f"⚠️  {cmd[2]} işlemi bulunamadı.")
        except Exception as e:
            print(f"❌ {cmd[2]} kapatılırken hata: {e}")
    
    # Port kontrolü
    time.sleep(1)
    try:
        result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
        if ':5000' in result.stdout:
            print("⚠️  Port 5000 hala aktif olabilir.")
        else:
            print("✅ Port 5000 serbest.")
    except:
        pass
    
    print("✅ Chatbot kapatma işlemi tamamlandı!")

if __name__ == "__main__":
    stop_chatbot() 