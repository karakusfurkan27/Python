import math

def silindir_hacmi(yukseklik, yaricap):
    hacim = math.pi * yaricap**2 * yukseklik
    return hacim

# Kullanıcıdan verileri alalım
yaricap = float(input("Silindirin yariçapini girin: "))
yukseklik = float(input("Silindirin yüksekliğini girin: "))

# Hacmi hesaplayalım
hacim = silindir_hacmi(yukseklik, yaricap)

print(f"Silindirin hacmi: {hacim:.2f} birim küp")