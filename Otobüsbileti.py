def bilet_fiyati_hesapla(bilet_fiyati, yolcu_sayisi, mesafe=None, indirim_orani=0):
    toplam_fiyat = bilet_fiyati * yolcu_sayisi
    
    # İndirim uygulanacaksa
    if indirim_orani > 0:
        indirim = toplam_fiyat * (indirim_orani / 100)
        toplam_fiyat -= indirim
    
    # Eğer mesafe üzerinden ek bir ücret eklenecekse
    if mesafe:
        mesafe_ucreti = mesafe * 0.10  # km başına 0.10 TL ücret diyelim
        toplam_fiyat += mesafe_ucreti
    
    return toplam_fiyat

# Örnek kullanım:
bilet_fiyati = 100  # 100 TL bilet fiyatı
yolcu_sayisi = 2
mesafe = 300  # 300 km
indirim_orani = 10  # %10 indirim

toplam_fiyat = bilet_fiyati_hesapla(bilet_fiyati, yolcu_sayisi, mesafe, indirim_orani)
print(f"Toplam Bilet Fiyati: {toplam_fiyat} TL")
