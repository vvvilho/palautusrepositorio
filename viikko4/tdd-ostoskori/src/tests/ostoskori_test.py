import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("maito", 3)
        self.leipa = Tuote("leipä", 2)
        self.keksi = Tuote("keksi", 1)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(),1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_oikea_hinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi(self):
        self.kori.lisaa_tuote(self.keksi)
        self.kori.lisaa_tuote(self.keksi)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_oikea_hinta(self):
        self.kori.lisaa_tuote(self.keksi)
        self.kori.lisaa_tuote(self.keksi)
        self.assertEqual(self.kori.hinta(), 2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostos_nimi_ja_lukumaara(self):
        self.kori.lisaa_tuote(self.maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_yksi_ostos(self):
        self.kori.lisaa_tuote(self.keksi)
        self.kori.lisaa_tuote(self.keksi)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostos_nimi_ja_lukumaara(self):
        self.kori.lisaa_tuote(self.keksi)
        self.kori.lisaa_tuote(self.keksi)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.keksi.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    def test_poista_yksi_saman_tuotteen_kahdesta_kappaleesta(self):
        self.kori.lisaa_tuote(self.keksi)
        self.kori.lisaa_tuote(self.keksi)
        self.kori.poista_tuote(self.keksi)
        self.assertEqual(len(self.kori.ostokset()), 1)
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)

    def test_lisaa_ja_poista_tuote_jattaa_korin_tyhjaksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)
        self.assertEqual(self.kori.ostokset(), [])
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)

    def test_tyhjenna_tyhjentaa_ostoskori(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.ostokset(), [])
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
    
