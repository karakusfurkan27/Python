import random

def bulmaca_oyunu():
    # Tahmin edilmesi gereken kelime listesi
    kelimeler = ["bilgisayar","python","algoritma","yazilim","veri"]
    
    # Rastgele bir kelime seç
    secilen_kelime = random.choice(kelimeler)

    # Kelimenin harflerini karıştır
    karisik_kelime = ''.join(random.sample(secilen_kelime, len(secilen_kelime)))

    print("Bulmaca Oyunu'na Hoş Geldiniz!")
    print("Bu karişik harflerden oluşan kelimeyi çözmeye çalişin: ",karisik_kelime)

    # Kullanıcıdan tahmin al
    tahmin = input("Kelimeyi tahmin edin: ")

    # Tahmin kontrol
    if tahmin.lower() == secilen_kelime:
        print("Tebrikler! Doğru tahmin.")

    else:
        print(f"Maalesef, doğru cevap '{secilen_kelime}' idi.")

# Oyunu başlat
bulmaca_oyunu        