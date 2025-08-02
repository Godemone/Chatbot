#!/usr/bin/env python3
"""
Chatbot Kapatma Scripti
Bu script chatbot'u güvenli bir şekilde kapatır.
"""

import os
import sys
import signal
import subprocess
import time
import psutil

def find_chatbot_processes():
    """Chatbot işlemlerini bul"""
    chatbot_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # Python işlemlerini kontrol et
            if proc.info['name'] and 'python' in proc.info['name'].lower():
                cmdline = proc.info['cmdline']
                if cmdline and any('app.py' in arg for arg in cmdline):
                    chatbot_processes.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return chatbot_processes

def check_port_5000():
    """Port 5000'de çalışan işlemleri kontrol et"""
    port_processes = []
    
    for conn in psutil.net_connections():
        if conn.laddr.port == 5000 and conn.status == 'LISTEN':
            try:
                proc = psutil.Process(conn.pid)
                port_processes.append(proc)
            except psutil.NoSuchProcess:
                continue
    
    return port_processes

def stop_processes(processes, process_type="Chatbot"):
    """İşlemleri güvenli bir şekilde durdur"""
    if not processes:
        print(f"❌ {process_type} işlemi bulunamadı.")
        return False
    
    print(f"🔍 {len(processes)} adet {process_type} işlemi bulundu:")
    
    for proc in processes:
        try:
            print(f"   - PID: {proc.pid}, İsim: {proc.name()}")
        except psutil.NoSuchProcess:
            continue
    
    # Kullanıcıdan onay al
    response = input(f"\n{process_type} işlemlerini durdurmak istiyor musunuz? (y/N): ")
    if response.lower() not in ['y', 'yes', 'evet', 'e']:
        print("❌ İşlem iptal edildi.")
        return False
    
    # İşlemleri durdur
    stopped_count = 0
    for proc in processes:
        try:
            print(f"🛑 PID {proc.pid} durduruluyor...")
            proc.terminate()  # Güvenli kapatma
            time.sleep(2)  # Biraz bekle
            
            # Hala çalışıyorsa zorla kapat
            if proc.is_running():
                print(f"⚠️  PID {proc.pid} zorla kapatılıyor...")
                proc.kill()
            
            stopped_count += 1
            print(f"✅ PID {proc.pid} başarıyla durduruldu.")
            
        except psutil.NoSuchProcess:
            print(f"⚠️  PID {proc.pid} zaten kapanmış.")
        except psutil.AccessDenied:
            print(f"❌ PID {proc.pid} için yetki yok.")
        except Exception as e:
            print(f"❌ PID {proc.pid} durdurulurken hata: {e}")
    
    return stopped_count > 0

def main():
    """Ana fonksiyon"""
    print("🤖 Chatbot Kapatma Aracı")
    print("=" * 40)
    
    # Chatbot işlemlerini bul
    chatbot_processes = find_chatbot_processes()
    port_processes = check_port_5000()
    
    if not chatbot_processes and not port_processes:
        print("✅ Chatbot zaten çalışmıyor.")
        return
    
    # İşlemleri durdur
    stopped_chatbot = False
    stopped_port = False
    
    if chatbot_processes:
        stopped_chatbot = stop_processes(chatbot_processes, "Chatbot")
    
    if port_processes:
        stopped_port = stop_processes(port_processes, "Port 5000")
    
    # Sonuçları göster
    print("\n" + "=" * 40)
    if stopped_chatbot or stopped_port:
        print("✅ Chatbot başarıyla kapatıldı!")
        
        # Kontrol et
        time.sleep(1)
        remaining_processes = find_chatbot_processes()
        remaining_ports = check_port_5000()
        
        if not remaining_processes and not remaining_ports:
            print("✅ Tüm işlemler temizlendi.")
        else:
            print("⚠️  Bazı işlemler hala çalışıyor olabilir.")
    else:
        print("❌ Chatbot kapatılamadı.")

def simple_stop():
    """Basit kapatma fonksiyonu"""
    print("🛑 Chatbot kapatılıyor...")
    
    try:
        # Windows için taskkill komutu
        result = subprocess.run(['taskkill', '/f', '/im', 'python3.13.exe'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Chatbot başarıyla kapatıldı!")
        else:
            print("⚠️  Python işlemi bulunamadı veya zaten kapanmış.")
            
    except Exception as e:
        print(f"❌ Hata: {e}")

if __name__ == "__main__":
    # psutil kütüphanesi yüklü mü kontrol et
    try:
        import psutil
        main()
    except ImportError:
        print("⚠️  psutil kütüphanesi yüklü değil. Basit kapatma kullanılıyor...")
        simple_stop() 