# Telefon rehberi sözlüğü
telefon_rehberi = {}

def kisi_ekle(isim, numara):
    telefon_rehberi[isim] = numara
    print(f"{isim} adlı kişi başarıyla eklendi.")

def kisi_sil(isim):
    if isim in telefon_rehberi:
        del telefon_rehberi[isim]
        print(f"{isim} adlı kişi başarıyla silindi.")
    else:
        print(f"{isim} adlı kişi bulunamadı.")

def kisi_ara(isim):
    if isim in telefon_rehberi:
        print(f"{isim} numarası: {telefon_rehberi[isim]}")
    else:
        print(f"{isim} adlı kişi bulunamadı.")

def tum_kisileri_listele():
    if telefon_rehberi:
        print("Telefon Rehberi:")
        for isim, numara in telefon_rehberi.items():
            print(f"{isim}: {numara}")
    else:
        print("Rehber boş.")

# Ana döngü
while True:
    print("\nTelefon Rehberi Uygulaması")
    print("1. Kişi Ekle")
    print("2. Kişi Sil")
    print("3. Kişi Ara")
    print("4. Tüm Kişileri Listele")
    print("5. Çıkış")
    secim = input("Bir seçim yapın (1-5): ")

    if secim == "1":
        isim = input("İsim: ")
        numara = input("Numara: ")
        kisi_ekle(isim, numara)
    elif secim == "2":
        isim = input("Silmek istediğiniz kişinin ismi: ")
        kisi_sil(isim)
    elif secim == "3":
        isim = input("Aramak istediğiniz kişinin ismi: ")
        kisi_ara(isim)
    elif secim == "4":
        tum_kisileri_listele()
    elif secim == "5":
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
        