import sqlite3

baglan=sqlite3.connect("veri.db")
if baglan:
    print ("Bağlanti Başarılı....")
else:
    print ("Bağlanti Başarısız....")

veri=baglan.cursor()
veri.execute('''
CREATE TABLE sinif(
sinif_no INTEGER PRIMARY KEY,
sinif_adi VARCHAR(5))            
''') 
#erkan çalışkan 