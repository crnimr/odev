import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

# Insan nesneleri oluşturma
insan1 = Insan("12345678901", "Ali", "Yılmaz", 30, "Erkek", "Türk")
insan2 = Insan("98765432109", "Ayşe", "Kara", 25, "Kadın", "Türk")

# İssiz nesneleri oluşturma
issiz1 = Issiz("11111111111", "Ahmet", "Demir", 35, "Erkek", "Türk", {"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 6})
issiz2 = Issiz("22222222222", "Mehmet", "Yılmaz", 28, "Erkek", "Türk", {"mavi yaka": 3, "beyaz yaka": 5, "yönetici": 7})
issiz3 = Issiz("33333333333", "Zeynep", "Öztürk", 31, "Kadın", "Türk", {"mavi yaka": 1, "beyaz yaka": 3, "yönetici": 5})

# Calisan nesneleri oluşturma
calisan1 = Calisan("44444444444", "Deniz", "Arslan", 42, "Erkek", "Türk", "teknoloji", 36, 20000)
calisan2 = Calisan("55555555555", "Ebru", "Kaya", 29, "Kadın", "Türk", "muhasebe", 18, 12000)
calisan3 = Calisan("66666666666", "Mustafa", "Şahin", 38, "Erkek", "Türk", "inşaat", 48, 30000)

# MaviYaka nesneleri oluşturma
mavi_yaka1 = MaviYaka("77777777777", "Can", "Yıldız", 33, "Erkek", "Türk", "Bilişim", 5, 15000, 0.2)
mavi_yaka2 = MaviYaka("88888888888", "Ayşe", "Demir", 28, "Kadın", "Türk", "Pazarlama", 3, 12000, 0.1)
mavi_yaka3 = MaviYaka("99999999999", "Mehmet", "Aksoy", 40, "Erkek", "Türk", "Finans", 8, 18000, 0.3)

# BeyazYaka nesneleri oluşturma
beyaz_yaka1 = BeyazYaka("12312312312", "Ayşe", "Demir", 36, "Kadın", "Türk", 4500, 500,1)
beyaz_yaka2 = BeyazYaka("45645645645", "Mehmet", "Kara", 40, "Erkek", "Türk", 6000, 500,4)
beyaz_yaka3 = BeyazYaka("78978978978", "Fatma", "Yılmaz", 32, "Kadın", "Türk", 5000, 2500,2)

# DataFrame oluşturma
data = {
    "Nesne Değeri": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
    "TC No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
    "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
    "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
    "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
    "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
    "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
    "Sektör": ["Teknoloji", "Satış", "Mühendislik", "Üretim", "Üretim", "Lojistik", "Finans", "Pazarlama", "İnsan Kaynakları"],
    "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
    "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
    "Yıpranma Payı": [0, 0, 0, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), 0, 0, 0],
    "Teşvik Prim": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
    "Yeni Maaş": [calisan1.zam_hakki(), calisan2.zam_hakki(), calisan3.zam_hakki(), mavi_yaka1.zam_hakki(), mavi_yaka2.zam_hakki(), mavi_yaka3.zam_hakki(), beyaz_yaka1.zam_hakki(), beyaz_yaka2.zam_hakki(), beyaz_yaka3.zam_hakki()]
}

df = pd.DataFrame(data)
