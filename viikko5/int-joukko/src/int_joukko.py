KAPASITEETTI = 5
OLETUS_KAPASITEETTI = 5
OLETUS_KASVATUSKOKO = 5

class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkioiden_maara = 0
        self.alkiot = self._luo_tyhja_lista(kapasiteetti)

    def _luo_tyhja_lista(self, koko):
        return [0] * koko

    def kuuluu(self, alkio):
        for i in range(self.alkioiden_maara):
            if self.alkiot[i] == alkio:
                return True
        return False

    def _kasvata_taulukkoa(self):
        uusi_koko = len(self.alkiot) + self.kasvatuskoko
        uusi_taulukko = self._luo_tyhja_lista(uusi_koko)

        for i in range(self.alkioiden_maara):
            uusi_taulukko[i] = self.alkiot[i]
        
        self.alkiot = uusi_taulukko

    def lisaa(self, alkio):
        if self.alkioiden_maara == len(self.alkiot):
            self._kasvata_taulukkoa()

        if not self.kuuluu(alkio):
            self.alkiot[self.alkioiden_maara] = alkio
            self.alkioiden_maara += 1
            return True
        return False

    def poista(self, alkio):
        for i in range(self.alkioiden_maara):
            if self.alkiot[i] == alkio:
                for j in range(i, self.alkioiden_maara - 1):
                    self.alkiot[j] = self.alkiot[j + 1]

                self.alkiot[self.alkioiden_maara - 1] = 0
                self.alkioiden_maara -= 1
                return True
        return False

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        return self.alkiot[:self.alkioiden_maara]

    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        elif self.alkioiden_maara == 1:
            return "{" + str(self.alkiot[0]) + "}"
        else:
            tuotos = "{"
            for i in range(self.alkioiden_maara - 1):
                tuotos += str(self.alkiot[i]) + ", "
            tuotos += str(self.alkiot[self.alkioiden_maara - 1]) + "}"
            return tuotos

    @staticmethod
    def yhdiste(a, b):
        yhdistetty = IntJoukko()
        for alkio in a.to_int_list() + b.to_int_list():
            yhdistetty.lisaa(alkio)
        return yhdistetty

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        for alkio in a.to_int_list():
            if b.kuuluu(alkio):
                leikkaus.lisaa(alkio)
        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        for alkio in a.to_int_list():
            if not b.kuuluu(alkio):
                erotus.lisaa(alkio)
        return erotus

    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        elif self.alkioiden_maara == 1:
            return "{" + str(self.alkiot[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_maara - 1):
                tuotos = tuotos + str(self.alkiot[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.alkiot[self.alkioiden_maara - 1])
            tuotos = tuotos + "}"
            return tuotos
