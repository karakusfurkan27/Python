import time
import random
import csv
from flask import Flask, render_template, request, redirect, url_for, send_file
import matplotlib.pyplot as plt
import pandas as pd
import threading
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from sklearn.linear_model import LinearRegression
import numpy as np

# Flask uygulaması
app = Flask(__name__)

# Flask-Mail yapılandırması
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

# Flask oturum yönetimi yapılandırması
login_manager = LoginManager()
login_manager.init_app(app)

# Kullanıcı sınıfı
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Oturumdan kullanıcıyı yükleme
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Global değişkenler
energy_data = []
time_labels = []
energy_goal = None
carbon_emission_rate = 0.5  # kWh başına CO2 emisyonu (örnek)

# Enerji tüketimi simülatörü (sensör yerine)
def get_energy_data():
    return round(random.uniform(0.5, 5.0), 2)  # kWh

# Verileri kaydetmek için CSV dosyasına yazma
def save_to_csv(data):
    with open("energy_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Enerji tasarrufu önerileri oluşturma
def suggest_savings(energy_data):
    high_usage_threshold = 3.5  # kWh
    suggestions = []
    for i, usage in enumerate(energy_data):
        if usage > high_usage_threshold:
            suggestions.append(f"Consider reducing usage at {time_labels[i]} to save energy.")
    return suggestions

# Enerji tüketimi tahmin fonksiyonu (Lineer Regresyon)
def predict_energy_usage():
    global energy_data, time_labels
    if len(energy_data) < 2:  # Yeterli veri olmadığında tahmin yapma
        return None
    
    # Veriyi zaman indeksine dönüştürme
    X = np.array(range(len(energy_data))).reshape(-1, 1)
    y = np.array(energy_data)
    
    # Lineer regresyon modeli oluşturma
    model = LinearRegression()
    model.fit(X, y)
    
    # Gelecek 10 veri noktası için tahmin yapma
    future_time = np.array(range(len(energy_data), len(energy_data) + 10)).reshape(-1, 1)
    predicted_energy = model.predict(future_time)
    
    return predicted_energy.tolist()

# E-posta bildirimi gönderme fonksiyonu
def send_email_notification(subject, body, recipient):
    msg = Message(subject, sender="your-email@gmail.com", recipients=[recipient])
    msg.body = body
    mail.send(msg)

# Karbon ayak izi hesaplama
def calculate_carbon_footprint(energy_data):
    return sum(energy_data) * carbon_emission_rate

# Flask route: Ana sayfa
@app.route("/")
def dashboard():
    global energy_data, time_labels, energy_goal
    suggestions = suggest_savings(energy_data)
    carbon_footprint = calculate_carbon_footprint(energy_data)
    return render_template("dashboard.html", energy_data=energy_data, time_labels=time_labels, 
                           suggestions=suggestions, energy_goal=energy_goal, carbon_footprint=carbon_footprint)

# Flask route: Verileri grafikte göster
@app.route("/plot")
def plot_data():
    global energy_data, time_labels
    plt.figure(figsize=(10, 6))
    plt.plot(time_labels, energy_data, marker="o", color="green", label="Energy Consumption (kWh)")
    plt.title("Energy Consumption Over Time")
    plt.xlabel("Time")
    plt.ylabel("Energy (kWh)")
    plt.grid(True)
    plt.legend()
    plt.savefig("static/energy_plot.png")
    plt.close()
    return render_template("plot.html", plot_url="/static/energy_plot.png")

# Flask route: Enerji tahminleri
@app.route("/predict")
def predict():
    predicted_energy = predict_energy_usage()
    if predicted_energy:
        return render_template("prediction.html", predictions=predicted_energy)
    else:
        return render_template("prediction.html", predictions=["Not enough data for prediction."])

# Flask route: Enerji hedefi belirleme
@app.route("/set_goal", methods=["POST"])
def set_goal():
    global energy_goal
    energy_goal = float(request.form["goal"])
    return redirect(url_for("dashboard"))

# Flask route: Enerji verisini CSV olarak dışa aktarma
@app.route("/export")
def export_data():
    global energy_data, time_labels
    with open('exported_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Energy"])
        for i in range(len(energy_data)):
            writer.writerow([time_labels[i], energy_data[i]])
    return send_file('exported_data.csv', as_attachment=True)

# Gerçek zamanlı veri toplama (arka planda çalıştırılabilir)
def collect_data():
    global energy_data, time_labels, energy_goal
    while True:
        current_time = time.strftime("%H:%M:%S")
        energy = get_energy_data()
        energy_data.append(energy)
        time_labels.append(current_time)
        save_to_csv([current_time, energy])  # Veriyi kaydet
        print(f"Collected Data: {current_time} - {energy} kWh")

        # Enerji limiti aşıldığında bildirim gönderme
        if energy_goal and energy > energy_goal:
            send_email_notification(
                "Energy Usage Alert",
                f"Your energy consumption has exceeded the target of {energy_goal} kWh. Current usage: {energy} kWh.",
                "recipient-email@example.com"
            )
        time.sleep(10)  # Her 10 saniyede bir veri toplar

# Flask uygulamasını başlatma
if __name__ == "__main__":
    # Veri toplama işlemini ayrı bir thread'de çalıştır
    data_thread = threading.Thread(target=collect_data, daemon=True)
    data_thread.start()
    app.run(debug=True)
