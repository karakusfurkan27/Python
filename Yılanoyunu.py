import pygame # type: ignore
import time
import random

# Pygame'i başlat
pygame.init()

# Renkler
beyaz = (255, 255, 255)
siyah = (0, 0, 0)
kırmızı = (213, 50, 80)
yeşil = (0, 255, 0)
mavi = (50, 153, 213)

# Oyun ekranı boyutları
genislik = 800
yukseklik = 600

# Ekran oluşturma
dis = pygame.display.set_mode((genislik, yukseklik))
pygame.display.set_caption('Yılan Oyunu')

# Saat objesi
saat = pygame.time.Clock()

# Yılanın boyutları ve hızı
yilan_hiz = 15
yilan_kalinlik = 10

# Yazı tipi
font_style = pygame.font.SysFont(None, 50)

# Mesajı ekranda gösteren fonksiyon
def mesaj(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [genislik / 6, yukseklik / 3])

# Oyunu başlatan fonksiyon
def oyun():
    oyun_bitti = False
    oyun_kapandi = False

    x1 = genislik / 2
    y1 = yukseklik / 2

    x1_degis = 0
    y1_degis = 0

    yilan_uzunlugu = 1
    yilan_vucudu = []

    yem_x = round(random.randrange(0, genislik - yilan_kalinlik) / 10.0) * 10.0
    yem_y = round(random.randrange(0, yukseklik - yilan_kalinlik) / 10.0) * 10.0

    while not oyun_bitti:

        while oyun_kapandi == True:
            dis.fill(siyah)
            mesaj("Oyun Bitti! Q ile çık, C ile devam et", kırmızı)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        oyun_bitti = True
                        oyun_kapandi = False
                    if event.key == pygame.K_c:
                        oyun()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_bitti = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_degis = -yilan_kalinlik
                    y1_degis = 0
                elif event.key == pygame.K_RIGHT:
                    x1_degis = yilan_kalinlik
                    y1_degis = 0
                elif event.key == pygame.K_UP:
                    y1_degis = -yilan_kalinlik
                    x1_degis = 0
                elif event.key == pygame.K_DOWN:
                    y1_degis = yilan_kalinlik
                    x1_degis = 0

        if x1 >= genislik or x1 < 0 or y1 >= yukseklik or y1 < 0:
            oyun_kapandi = True

        x1 += x1_degis
        y1 += y1_degis
        dis.fill(siyah)
        pygame.draw.rect(dis, yeşil, [yem_x, yem_y, yilan_kalinlik, yilan_kalinlik])
        
        yilan_bas = []
        yilan_bas.append(x1)
        yilan_bas.append(y1)
        yilan_vucudu.append(yilan_bas)
        if len(yilan_vucudu) > yilan_uzunlugu:
            del yilan_vucudu[0]

        for parca in yilan_vucudu[:-1]:
            if parca == yilan_bas:
                oyun_kapandi = True

        for x in yilan_vucudu:
            pygame.draw.rect(dis, beyaz, [x[0], x[1], yilan_kalinlik, yilan_kalinlik])

        pygame.display.update()

        if x1 == yem_x and y1 == yem_y:
            yem_x = round(random.randrange(0, genislik - yilan_kalinlik) / 10.0) * 10.0
            yem_y = round(random.randrange(0, yukseklik - yilan_kalinlik) / 10.0) * 10.0
            yilan_uzunlugu += 1

        saat.tick(yilan_hiz)

    pygame.quit()
    quit()

oyun()
