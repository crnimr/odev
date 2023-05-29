from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def statu_bul(self):
        max_statu = max(self.__tecrube, key=self.__tecrube.get)
        return max_statu

    def __str__(self):
        return f"Issiz: {self.get_tc_no()}, {self.get_ad()}, {self.get_soyad()}, {self.get_yas()}, {self.get_cinsiyet()}, {self.get_uyruk()}, Tecrube: {self.__tecrube}"
