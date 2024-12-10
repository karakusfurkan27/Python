import sqlite3

baglanti = sqlite3.connect("arabalar.db") #veri tabanına baglanma
islem = baglanti.cursor()
baglanti.commit

# if not exists arabalar adlı tablo varsa devam et yoksa olustur
table = islem.execute("create table if not exists arabalar (Marka text, Model text, Renk text,Km int)")
baglanti.commit()

def veri_ekle(Marka,Model,Renk,Km):
    kayit = "insert into arabalar values (?,?,?,?)"
    islem.execute(kayit,(Marka,Model,Renk,Km)) #veri tabanına ekleme
    baglanti.commit()

    