import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_ostokset_varaston_tuotteella_asiakkaan_tiedoilla(self):
            pankki_mock = Mock()
            viitegeneraattori_mock = Mock()

            # palautetaan aina arvo 42
            viitegeneraattori_mock.uusi.return_value = 42

            varasto_mock = Mock()

            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)

            # otetaan toteutukset käyttöön
            varasto_mock.saldo.side_effect = varasto_saldo
            varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            # lisätään ostoskoriin tuote, jonka id on 1
            kauppa.lisaa_koriin(1)
            kauppa.tilimaksu("pekka", "12345")
            
            pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kaksi_samaa_tuotetta(self):
            pankki_mock = Mock()
            viitegeneraattori_mock = Mock()

            # palautetaan aina arvo 42
            viitegeneraattori_mock.uusi.return_value = 42

            varasto_mock = Mock()

            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10
                elif tuote_id == 2:
                    return 10

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)
                elif tuote_id == 2:
                    return Tuote(2, "piimä", 10)

            # otetaan toteutukset käyttöön
            varasto_mock.saldo.side_effect = varasto_saldo
            varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            # lisätään ostoskoriin tuote, jonka id on 1
            kauppa.lisaa_koriin(1)
            kauppa.lisaa_koriin(1)
            kauppa.tilimaksu("pekka", "12345")
            
            pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)


    def test_kaksi_eri_tuotetta(self):
            pankki_mock = Mock()
            viitegeneraattori_mock = Mock()

            # palautetaan aina arvo 42
            viitegeneraattori_mock.uusi.return_value = 42

            varasto_mock = Mock()

            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10
                elif tuote_id == 2:
                    return 10

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)
                elif tuote_id == 2:
                    return Tuote(2, "piimä", 10)

            # otetaan toteutukset käyttöön
            varasto_mock.saldo.side_effect = varasto_saldo
            varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            # lisätään ostoskoriin tuote, jonka id on 1
            kauppa.lisaa_koriin(1)
            kauppa.lisaa_koriin(2)
            kauppa.tilimaksu("pekka", "12345")
            
            pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 15)

    def test_kaksi_eri_tuotetta_toinen_loppu(self):
            pankki_mock = Mock()
            viitegeneraattori_mock = Mock()

            # palautetaan aina arvo 42
            viitegeneraattori_mock.uusi.return_value = 42

            varasto_mock = Mock()

            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10
                elif tuote_id == 2:
                    return 0

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)
                elif tuote_id == 2:
                    return Tuote(2, "piimä", 10)

            # otetaan toteutukset käyttöön
            varasto_mock.saldo.side_effect = varasto_saldo
            varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            # lisätään ostoskoriin tuote, jonka id on 1
            kauppa.lisaa_koriin(1)
            kauppa.lisaa_koriin(2)
            kauppa.tilimaksu("pekka", "12345")
            
            pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "piimä", 10)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # Ensimmäinen asiointi
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)  # lisää maito
        kauppa.tilimaksu("pekka", "12345")

        # Varmistetaan, että tilisiirtoa kutsutaan oikeilla arvoilla
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

        # Aloitetaan uusi asiointi, joka pitäisi nollata edellisen ostoksen tiedot
        pankki_mock.reset_mock()  # Nollataan pankkimockin kutsut

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)  # lisää leipä
        kauppa.tilimaksu("pekka", "12345")

        # Varmistetaan, että tilisiirtoa kutsutaan oikeilla arvoilla
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_uusi_viitenumero_jokaiselle_maksutapahtumalle(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # Määritellään viitegeneraattori palauttamaan eri viitenumerot
        viitegeneraattori_mock.uusi.side_effect = [42, 43]

        varasto_mock = Mock()

        # Tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5

        # Tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "piimä", 10)

        # Otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # Alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # Ensimmäinen asiointi
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)  # Lisää maito
        kauppa.tilimaksu("pekka", "12345")

        # Varmistetaan, että tilisiirtoa kutsutaan oikeilla arvoilla
        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

        # Aloitetaan uusi asiointi
        pankki_mock.reset_mock()  # Nollataan pankkimockin kutsut

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)  # Lisää leipä
        kauppa.tilimaksu("pekka", "12345")

        # Varmistetaan, että tilisiirtoa kutsutaan oikeilla arvoilla
        pankki_mock.tilisiirto.assert_called_with("pekka", 43, "12345", "33333-44455", 10)

    def test_poista_korista_poistaa_tuotteen(self):
            pankki_mock = Mock()
            viitegeneraattori_mock = Mock()

            # palautetaan aina arvo 42
            viitegeneraattori_mock.uusi.return_value = 42

            varasto_mock = Mock()

            # tehdään toteutus saldo-metodille
            def varasto_saldo(tuote_id):
                if tuote_id == 1:
                    return 10
                elif tuote_id == 2:
                    return 0

            # tehdään toteutus hae_tuote-metodille
            def varasto_hae_tuote(tuote_id):
                if tuote_id == 1:
                    return Tuote(1, "maito", 5)
                elif tuote_id == 2:
                    return Tuote(2, "piimä", 10)

            # otetaan toteutukset käyttöön
            varasto_mock.saldo.side_effect = varasto_saldo
            varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            # lisätään ostoskoriin tuote, jonka id on 1
            kauppa.lisaa_koriin(1)
            kauppa.poista_korista(1)
            kauppa.tilimaksu("pekka", "12345")
            
            pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 0)