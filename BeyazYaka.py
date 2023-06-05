class BeyazYaka:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk,maas,tesvik_primi,tecrube):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
        self.__maas=maas
        self.__tesvik_primi=tesvik_primi
        self.__tecrube=tecrube

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

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        if tesvik_primi == 500 or tesvik_primi == 2500:
            self.__tesvik_primi = tesvik_primi
            self.__tesvik_primi = tesvik_primi

        else:
            print("Hatalı teşvik primi değeri!")

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def zam_hakki(self):
        try:
            if self.__tecrube <= 2:
                zam_miktari = self.__tesvik_primi
            elif 2 < self.__tecrube <= 4 and self.__maas < 15000:
                zam_miktari = (self.__maas * self.__tecrube / 100) * 5 + self.__tesvik_primi
            elif self.__tecrube > 4 and self.__maas < 25000:
                zam_miktari = (self.__maas * self.__tecrube) / 25 + self.__tesvik_primi
            else:
                zam_miktari = 0

            yeni_maas = self.__maas + zam_miktari
            if yeni_maas == self.__maas:
                return self.__maas
            else:
                self.__maas = yeni_maas
                return yeni_maas

        except Exception as e:
            print("Hata: ", e)

    def __str__(self):
        try:
            yeni_maas = self.zam_hakki()
            return super().__str__() + f"\nAd: {self.__ad}\nSoyad: {self.__soyad}\nTecrübe: {self.__tecrube} ay\nYeni Maaş: {yeni_maas}"
        except Exception as e:
            return f"Hata: {e}"