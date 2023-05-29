from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube)
        self.__maas = maas
        self.__yipranma_payi = yipranma_payi

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        if self.get_tecrube() >= 2 and self.__maas < 15000:
            zam_orani = (self.__maas * self.get_tecrube() / 100) * 5 + (self.__yipranma_payi * 10)
        elif self.get_tecrube() > 4 and self.__maas < 25000:
            zam_orani = (self.__maas * self.get_tecrube()) / 25 + (self.__yipranma_payi * 10)
        else:
            zam_orani = self.__yipranma_payi * 10

        yeni_maas = self.__maas + zam_orani

        if yeni_maas == self.__maas:
            return self.__maas
        else:
            self.__maas = yeni_maas
            return yeni_maas

    def __str__(self):
        return f"Mavi Yaka: {self.get_tc_no()}, {self.get_ad()}, {self.get_soyad()}, {self.get_yas()}, {self.get_cinsiyet()}, {self.get_uyruk()}, Maas: {self.__maas}, Yipranma Payi: {self.__yipranma_payi}"
