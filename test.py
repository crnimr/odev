import unittest
import pandas as pd

from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka


class TestProje(unittest.TestCase):
    def test_insan(self):
        insan = Insan("12345678901", "John", "Doe", 30, "Erkek", "Türk")
        self.assertEqual(insan.tc_no, "12345678901")
        self.assertEqual(insan.ad, "John")
        self.assertEqual(insan.soyad, "Doe")
        self.assertEqual(insan.yas, 30)
        self.assertEqual(insan.cinsiyet, "Erkek")
        self.assertEqual(insan.uyruk, "Türk")

    def test_issiz(self):
        issiz = Issiz("12345678901", "John", "Doe", 30, "Erkek", "Türk", {"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 6})
        self.assertEqual(issiz.tc_no, "12345678901")
        self.assertEqual(issiz.ad, "John")
        self.assertEqual(issiz.soyad, "Doe")
        self.assertEqual(issiz.yas, 30)
        self.assertEqual(issiz.cinsiyet, "Erkek")
        self.assertEqual(issiz.uyruk, "Türk")
        self.assertEqual(issiz.statuler, {"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 6})
        self.assertEqual(issiz.statu_bul(), "yönetici")

    def test_calisan(self):
        calisan = Calisan("12345678901", "John", "Doe", 30, "Erkek", "Türk", "teknoloji", 36, 20000)
        self.assertEqual(calisan.tc_no, "12345678901")
        self.assertEqual(calisan.ad, "John")
        self.assertEqual(calisan.soyad, "Doe")
        self.assertEqual(calisan.yas, 30)
        self.assertEqual(calisan.cinsiyet, "Erkek")
        self.assertEqual(calisan.uyruk, "Türk")
        self.assertEqual(calisan.sektor, "teknoloji")
        self.assertEqual(calisan.tecrube, 36)
        self.assertEqual(calisan.maas, 20000)
        self.assertEqual(calisan.zam_hakki(), 0)
        self.assertEqual(calisan.yeni_maas, 20000)

    def test_mavi_yaka(self):
        mavi_yaka = MaviYaka("12345678901", "John", "Doe", 30, "Erkek", "Türk", "teknoloji", 36, 20000, 0.2)
        self.assertEqual(mavi_yaka.tc_no, "12345678901")
        self.assertEqual(mavi_yaka.ad, "John")
        self.assertEqual(mavi_yaka.soyad, "Doe")
        self.assertEqual(mavi_yaka.yas, 30)
        self.assertEqual(mavi_yaka.cinsiyet, "Erkek")
        self.assertEqual(mavi_yaka.uyruk, "Türk")
        self.assertEqual(mavi_yaka.sektor, "teknoloji")
        self.assertEqual(mavi_yaka.tecrube, 36)
        self.assertEqual(mavi_yaka.maas, 20000)
        self.assertEqual(mavi_yaka.zam_orani, 0.2)
        self.assertEqual(mavi_yaka.zam_hakki(), 7200)
        self.assertEqual(mavi_yaka.yeni_maas, 27200)

    def test_beyaz_yaka(self):
        beyaz_yaka = BeyazYaka("12345678901", "John", "Doe", 30, "Erkek", "Türk", "finans", 48, 30000, 0.15)
        self.assertEqual(beyaz_yaka.tc_no, "12345678901")
        self.assertEqual(beyaz_yaka.ad, "John")
        self.assertEqual(beyaz_yaka.soyad, "Doe")
        self.assertEqual(beyaz_yaka.yas, 30)
        self.assertEqual(beyaz_yaka.cinsiyet, "Erkek")
        self.assertEqual(beyaz_yaka.uyruk, "Türk")
        self.assertEqual(beyaz_yaka.sektor, "finans")
        self.assertEqual(beyaz_yaka.tecrube, 48)
        self.assertEqual(beyaz_yaka.maas, 30000)
        self.assertEqual(beyaz_yaka.zam_orani, 0.15)
        self.assertEqual(beyaz_yaka.zam_hakki(), 8640)
        self.assertEqual(beyaz_yaka.yeni_maas, 38640)

if __name__ == "__main__":
    unittest.main()