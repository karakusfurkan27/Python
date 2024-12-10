# Kullanıcıdan bilgileri al
ad = input("Adiniz: ")
yas = int(input("Yaşiniz: "))
# Ehliyet alabilme durumunu kontrol et
if yas < 18:
    print("Üzgünüm, yaşiniz ehliyet almak için yeterli değil.")
else:
    egitim = input("Eğitim Seviyeniz (İlköğretim, Ortaöğretim, Lise, Lisans, Ön Lisans, Yüksek Lisans, Doktora): ")
if egitim in ["Lise", "Lisans", "Yüksek Lisans", "Doktora", "Ön Lisans"]:
    print("Tebrikler! Ehliyet alabilirsiniz.")
else:
    print("Üzgünüm, eğitim seviyeniz ehliyet almak için yeterli değil.")