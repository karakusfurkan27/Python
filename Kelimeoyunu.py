import random

def karistir_kelime(kelime):
    kelime_listesi = list(kelime)
    random.shuffle(kelime_listesi)
    return ''.join(kelime_listesi)

def kelime_oyunu():
    kelime_listesi = ['elma', 'armut', 'muz', 'çilek', 'karpuz']
    secilen_kelime = random.choice(kelime_listesi)
    karisik_kelime = karistir_kelime(secilen_kelime)
    
    print("Karışık kelime: ", karisik_kelime)
    
    tahmin = input("Bu kelimenin doğru hali nedir? ")
    
    if tahmin == secilen_kelime:
        print("Tebrikler! Doğru bildiniz.")
    else:
        print("Maalesef, doğru cevap: ", secilen_kelime)

kelime_oyunu()
