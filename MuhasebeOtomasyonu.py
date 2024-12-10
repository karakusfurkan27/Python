import sqlite3
from datetime import datetime

# Veritabanı bağlantısı kur
conn = sqlite3.connect("muhasebe_otomasyonu.db")
cursor = conn.cursor()

# Gerekli tabloları oluştur
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    amount REAL,
    description TEXT,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS balance (
    id INTEGER PRIMARY KEY,
    total_balance REAL
)
""")

# Eğer bakiyeyi tutan tablo boşsa başlangıç değeri olarak 0 ekleyelim
cursor.execute("SELECT * FROM balance")
if cursor.fetchone() is None:
    cursor.execute("INSERT INTO balance (id, total_balance) VALUES (1, 0)")
    conn.commit()

# Gelir veya gider işlemi ekleme fonksiyonu
def add_transaction(transaction_type, amount, description):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO transactions (type, amount, description, date) VALUES (?, ?, ?, ?)",
                   (transaction_type, amount, description, date))
    # Bakiyeyi güncelle
    update_balance(transaction_type, amount)
    conn.commit()
    print(f"{transaction_type.capitalize()} başarıyla eklendi!")

# Bakiyeyi güncelleyen fonksiyon
def update_balance(transaction_type, amount):
    cursor.execute("SELECT total_balance FROM balance WHERE id = 1")
    current_balance = cursor.fetchone()[0]
    
    if transaction_type == "gelir":
        new_balance = current_balance + amount
    elif transaction_type == "gider":
        new_balance = current_balance - amount

    cursor.execute("UPDATE balance SET total_balance = ? WHERE id = 1", (new_balance,))
    conn.commit()

# Güncel bakiyeyi gösteren fonksiyon
def show_balance():
    cursor.execute("SELECT total_balance FROM balance WHERE id = 1")
    balance = cursor.fetchone()[0]
    print(f"Güncel Bakiye: {balance} TL")

# İşlemleri listeleme fonksiyonu
def list_transactions():
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    print("ID | Tür | Miktar | Açıklama | Tarih")
    print("-" * 50)
    for transaction in transactions:
        print(transaction)

# Ana menü
def main():
    while True:
        print("\n=== Muhasebe Otomasyonu ===")
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. İşlemleri Listele")
        print("4. Bakiye Görüntüle")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            amount = float(input("Gelir miktarını girin: "))
            description = input("Gelir açıklamasını girin: ")
            add_transaction("gelir", amount, description)

        elif choice == "2":
            amount = float(input("Gider miktarını girin: "))
            description = input("Gider açıklamasını girin: ")
            add_transaction("gider", amount, description)

        elif choice == "3":
            list_transactions()

        elif choice == "4":
            show_balance()

        elif choice == "5":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Programı başlat
if __name__ == "__main__":
    main()

# Veritabanı bağlantısını kapat
conn.close()
