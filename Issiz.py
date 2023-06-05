class Issiz:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk,tecrubeler):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
        self.__tecrubeler = tecrubeler

    def get_tc_no(self):
        return self.__tc_no

    def set_tc_no(self, tc_no):
        self.__tc_no = tc_no

    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_yas(self):
        return self.__yas

    def set_yas(self, yas):
        self.__yas = yas

    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    def get_uyruk(self):
        return self.__uyruk

    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    def get_tecrubeler(self):
        return self.__tecrubeler

    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler

    def statu_bul(self):
        try:
            statuler = {
                "mavi yaka": sum(self.__tecrubeler.values()) * 0.20,
                "beyaz yaka": sum(self.__tecrubeler.values()) * 0.35,
                "yönetici": sum(self.__tecrubeler.values()) * 0.45
            }
            en_uygun_statu = max(statuler, key=statuler.get)
            return en_uygun_statu
        except Exception as e:
            print(f"Hata: {e}")
            return None

    def __str__(self):
        en_uygun_statu = self.statu_bul()
        if en_uygun_statu:
            return f"Ad: {self.__ad}\nSoyad: {self.__soyad}\nEn Uygun Statü: {en_uygun_statu}"
        else:
            return f"Ad: {self.__ad}\nSoyad: {self.__soyad}\nEn Uygun Statü Bulunamadı"


