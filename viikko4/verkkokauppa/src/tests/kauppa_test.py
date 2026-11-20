import unittest
from unittest.mock import Mock, call
from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipa", 7),
        }
        self.saldot = {1: 10, 2: 10}
        self.varasto_mock = Mock()
        self.varasto_mock.saldo.side_effect = lambda tuote_id: self.saldot.get(tuote_id, 0)
        self.varasto_mock.hae_tuote.side_effect = self.tuotteet.get

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )
        self.kauppa.aloita_asiointi()

    def suorita_ostos(self, *tuote_idt):
        self.kauppa.aloita_asiointi()
        for tuote_id in tuote_idt:
            self.kauppa.lisaa_koriin(tuote_id)
        self.kauppa.tilimaksu("pekka", "12345")

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.suorita_ostos(1)

        self.pankki_mock.tilisiirto.assert_called_once()

    def test_maksettaessa_pankin_metodia_tilisiirto_kutsutaan_oikealla_tilinumerolla(self):
        self.suorita_ostos(1)

        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_maksettaessa_kahdella_tuotteella_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        self.suorita_ostos(1, 2)

        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 12
        )

    def test_maksettaessa_kahdella_samalla_tuotteella_tilisiirto_kutsutaan_oikeilla_tiedoilla(self):
        self.suorita_ostos(1, 1)

        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_jokaiselle_maksutapahtumalle_pyydetaan_uusi_viitenumero(self):
        self.viitegeneraattori_mock.uusi.side_effect = [42, 43]

        self.suorita_ostos(1)
        self.suorita_ostos(2)

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)
        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list,
            [
                call("pekka", 42, "12345", "33333-44455", 5),
                call("pekka", 43, "12345", "33333-44455", 7),
            ],
        )

    def test_loppunut_tuote_ei_mene_ostoskoriin_eika_nosta_maksun_summaa(self):
        self.saldot[1] = 1
        self.saldot[2] = 0

        self.suorita_ostos(1, 2)

        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 5
        )
        self.varasto_mock.ota_varastosta.assert_called_once_with(self.tuotteet[1])

    def test_aloita_asiointi_nollaa_ostoskoriin_kertyneet_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)

        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 0
        )

    def test_poista_korista_palauttaa_tuotteen_varastoon(self):
        self.kauppa.lisaa_koriin(1)

        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.varasto_mock.palauta_varastoon.assert_called_once_with(self.tuotteet[1])
        self.pankki_mock.tilisiirto.assert_called_once_with(
            "pekka", 42, "12345", "33333-44455", 0
        )
