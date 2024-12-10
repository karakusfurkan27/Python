import time
import random
import csv
from flask import Flask, render_template, request, redirect, url_for, send_file
import matplotlib.pyplot as plt
import pandas as pd
import threading
from flask_mail import Mail, Message # type: ignore
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
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

# Enerji tüketimi tahmin fonksiyonu (Linear Regression)
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

# Flask route: Ana sayfa
@app.route("/")
def dashboard():
    global energy_data, time_labels, energy_goal
    suggestions = suggest_savings(energy_data)
    return render_template("dashboard.html", energy_data=energy_data, time_labels=time_labels, suggestions=suggestions, energy_goal=energy_goal)

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

# Flask route: Tasarruf ipuçları ve bildirimler
@app.route("/savings")
def savings_tips():
    global energy_data, time_labels
    suggestions = suggest_savings(energy_data)
    return render_template("savings.html", suggestions=suggestions)

# Flask route: Verileri zaman dilimlerine göre göster
@app.route("/compare", methods=["GET", "POST"])
def compare_data():
    if request.method == "POST":
        start_time = request.form["start_time"]
        end_time = request.form["end_time"]
        filtered_data = filter_data_by_time(start_time, end_time)
        return render_template("compare.html", data=filtered_data)
    return render_template("compare_form.html")

def filter_data_by_time(start_time, end_time):
    global energy_data, time_labels
    filtered_data = []
    for i, time in enumerate(time_labels):
        if start_time <= time <= end_time:
            filtered_data.append((time, energy_data[i]))
    return filtered_data

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

# Flask route: CSV dosyasından veri yükleme
@app.route("/load_data", methods=["POST"])
def load_data():
    file = request.files['csv_file']
    data = pd.read_csv(file)
    time_labels.extend(data['time'].tolist())
    energy_data.extend(data['energy'].tolist())
    return render_template("dashboard.html", energy_data=energy_data, time_labels=time_labels)

# Flask route: Enerji verilerini filtreleme
@app.route("/filter", methods=["GET", "POST"])
def filter_data():
    if request.method == "POST":
        threshold = float(request.form["threshold"])
        global energy_data, time_labels
        filtered_data = [(time, energy) for time, energy in zip(time_labels, energy_data) if energy >= threshold]
        time_labels, energy_data = zip(*filtered_data)  # Filtrelenmiş veriyi kaydet
        return render_template("filtered_data.html", filtered_data=filtered_data)
    return render_template("filter_form.html")

# Flask route: Enerji tahminleri
@app.route("/predict")
def predict():
    predicted_energy = predict_energy_usage()
    if predicted_energy:
        return render_template("prediction.html", predictions=predicted_energy)
    else:
        return render_template("prediction.html", predictions=["Not enough data for prediction."])

# Flask route: E-posta bildirimi kontrolü
@app.route("/check_goal")
def check_goal():
    global energy_goal, energy_data
    if energy_goal and max(energy_data) > energy_goal:
        send_email_notification(
            "Energy Usage Alert",
            f"Your energy consumption has exceeded the target of {energy_goal} kWh.",
            "recipient-email@example.com"
        )
        return "Goal exceeded. Notification sent!"
    return "Energy consumption within the target range."

# Gerçek zamanlı veri toplama (arka planda çalıştırılabilir)
def collect_data():
    global energy_data, time_labels
    while True:
        current_time = time.strftime("%H:%M:%S")
        energy = get_energy_data()
        energy_data.append(energy)
        time_labels.append(current_time)
        save_to_csv([current_time, energy])  # Veriyi kaydet
        print(f"Collected Data: {current_time} - {energy} kWh")
        time.sleep(10)  # Her 10 saniyede bir veri toplar

# Flask uygulamasını başlatma
if __name__ == "__main__":
    # Veri toplama işlemini ayrı bir thread'de çalıştır
    data_thread = threading.Thread(target=collect_data, daemon=True)
    data_thread.start()
    app.run(debug=True)
