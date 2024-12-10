import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# OpenWeatherMap API bilgileri
API_KEY = 'your_api_key_here'
CITY = 'Gaziantep'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={GAZİANTEP}&appid={API_KEY}&units=metric' # type: ignore

# Uyarı e-posta bilgileri
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_password'
RECEIVER_EMAIL = 'receiver_email@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Hava durumu verilerini çekme
def get_weather_data():
    response = requests.get(URL)
    return response.json()

# Uyarı e-postası gönderme
def send_warning_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        server.quit()
        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"E-posta gönderilirken hata oluştu: {e}")

# Hava durumu kontrolü ve uyarı oluşturma
def check_weather_conditions():
    data = get_weather_data()
    
    temp = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    
    print(f"Sıcaklık: {temp}°C, Hava Durumu: {weather_desc}, Rüzgar Hızı: {wind_speed} m/s")
    
    # Belirli bir hava durumu koşulu için uyarı gönderme
    if temp < 0:
        send_warning_email(
            "Düşük Sıcaklık Uyarısı",
            f"Sıcaklık {temp}°C'ye düştü. Dışarı çıkarken dikkatli olun!"
        )
    elif wind_speed > 10:
        send_warning_email(
            "Şiddetli Rüzgar Uyarısı",
            f"Rüzgar hızı {wind_speed} m/s'e ulaştı. Dikkatli olun!"
        )

# Otomatik olarak sürekli kontrol yapma (örnek her 1 saatte bir kontrol)
import time

def run_weather_check(interval=3600):
    while True:
        check_weather_conditions()
        time.sleep(interval)

# Otomasyonu çalıştır
run_weather_check()
