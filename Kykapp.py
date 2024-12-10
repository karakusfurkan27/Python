import sqlite3

# KYK Yurt Sistemi Uygulaması
connection = sqlite3.connect("kyk_yurt_sistemi.db")
cursor = connection.cursor()

# Tablo oluşturma
cursor.execute('''
CREATE TABLE IF NOT EXISTS ogrenciler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    soyad TEXT NOT NULL,
    oda_no INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS yemekhane (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    yemek_adi TEXT NOT NULL,
    ogun TEXT NOT NULL,
    tarih DATE NOT NULL
)
''')

connection.commit()

# Fonksiyonlar
def ogrenci_ekle(ad, soyad, oda_no):
    """Yeni bir öğrenci ekler."""
    cursor.execute("INSERT INTO ogrenciler (ad, soyad, oda_no) VALUES (?, ?, ?)", (ad, soyad, oda_no))
    connection.commit()
    print(f"\nÖğrenci '{ad} {soyad}' başarıyla eklenmiştir.")

def ogrenci_sil(ogrenci_id):
    """Belirtilen ID'ye sahip öğrenciyi siler."""
    cursor.execute("DELETE FROM ogrenciler WHERE id = ?", (ogrenci_id,))
    connection.commit()
    print(f"\nID {ogrenci_id} olan öğrenci silinmiştir.")

def ogrenci_guncelle(ogrenci_id, yeni_ad, yeni_soyad, yeni_oda_no):
    """Belirtilen ID'ye sahip öğrencinin bilgilerini günceller."""
    cursor.execute("UPDATE ogrenciler SET ad = ?, soyad = ?, oda_no = ? WHERE id = ?", (yeni_ad, yeni_soyad, yeni_oda_no, ogrenci_id))
    connection.commit()
    print(f"\nID {ogrenci_id} olan öğrenci başarıyla güncellendi.")

def yemek_ekle(yemek_adi, ogun, tarih):
    """Yeni bir yemek ekler."""
    cursor.execute("INSERT INTO yemekhane (yemek_adi, ogun, tarih) VALUES (?, ?, ?)", (yemek_adi, ogun, tarih))
    connection.commit()
    print(f"\n'{yemek_adi}' ({ogun}) başarıyla eklenmiştir.")

def ogrenci_listesi():
    """Öğrenci listesini görüntüler."""
    cursor.execute("SELECT * FROM ogrenciler")
    ogrenciler = cursor.fetchall()
    print("\nÖğrenci Listesi:")
    for ogrenci in ogrenciler:
        print(f"ID: {ogrenci[0]}, Ad: {ogrenci[1]}, Soyad: {ogrenci[2]}, Oda No: {ogrenci[3]}")

def yemek_listesi():
    """Öğün listesini görüntüler."""
    cursor.execute("SELECT * FROM yemekhane")
    yemekler = cursor.fetchall()
    print("\nYemekhane Listesi:")
    for yemek in yemekler:
        print(f"ID: {yemek[0]}, Yemek: {yemek[1]}, Öğün: {yemek[2]}, Tarih: {yemek[3]}")

# Ana Menü
if __name__ == "__main__":
    while True:
        print("\n*** KYK Yurt Sistemi ***")
        print("1. Öğrenci Ekle")
        print("2. Öğrenci Sil")
        print("3. Öğrenci Güncelle")
        print("4. Öğrenci Listesi")
        print("5. Yemek Ekle")
        print("6. Yemek Listesi")
        print("7. Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            ad = input("Öğrenci Adı: ")
            soyad = input("Öğrenci Soyadı: ")
            oda_no = int(input("Oda No: "))
            ogrenci_ekle(ad, soyad, oda_no)
        elif secim == "2":
            ogrenci_id = int(input("Silmek istediğiniz Öğrenci ID: "))
            ogrenci_sil(ogrenci_id)
        elif secim == "3":
            ogrenci_id = int(input("Güncellemek istediğiniz Öğrenci ID: "))
            yeni_ad = input("Yeni Ad: ")
            yeni_soyad = input("Yeni Soyad: ")
            yeni_oda_no = int(input("Yeni Oda No: "))
            ogrenci_guncelle(ogrenci_id, yeni_ad, yeni_soyad, yeni_oda_no)
        elif secim == "4":
            ogrenci_listesi()
        elif secim == "5":
            yemek_adi = input("Yemek Adı: ")
            ogun = input("Öğün (Sabah/Öğle/Akşam): ")
            tarih = input("Tarih (YYYY-MM-DD): ")
            yemek_ekle(yemek_adi, ogun, tarih)
        elif secim == "6":
            yemek_listesi()
        elif secim == "7":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

connection.close()
