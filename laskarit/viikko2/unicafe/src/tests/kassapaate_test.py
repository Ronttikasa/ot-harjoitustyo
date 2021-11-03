import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.koyha_kortti = Maksukortti(10)
        self.rikas_kortti = Maksukortti(1000)

    def test_kassapaate_luotu_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    # edullisesti, käteisosto, rahaa tarpeeksi
    def test_syo_edullisesti_kateisella_toimii(self):
        takaisin = self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(takaisin, 260)

    # edullisesti, käteisosto, liian vähän rahaa
    def test_syo_edullisesti_kateisella_toimii_liian_pieni_maksu(self):
        takaisin = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(takaisin, 200)

    # maukkaasti, käteisosto, rahaa tarpeeksi
    def test_syo_maukkaasti_kateisella_toimii(self):
        takaisin = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(takaisin, 100)

    # maukkaasti, käteisosto, liian vähän rahaa
    def test_syo_maukkaasti_kateisella_toimii_liian_pieni_maksu(self):    
        takaisin = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(takaisin, 200)
    
    # edullisesti, korttimaksu
    def test_syo_edullisesti_kortilla_toimii(self):
        pal = self.kassa.syo_edullisesti_kortilla(self.rikas_kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(pal, True)
        self.assertEqual(self.rikas_kortti.saldo, 760)

    def test_syo_edullisesti_kortilla_liian_vahan_rahaa(self):
        pal = self.kassa.syo_edullisesti_kortilla(self.koyha_kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(pal, False)
        self.assertEqual(self.koyha_kortti.saldo, 10)

    def test_syo_maukkaasti_kortilla_toimii(self):
        pal = self.kassa.syo_maukkaasti_kortilla(self.rikas_kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(pal, True)
        self.assertEqual(self.rikas_kortti.saldo, 600)

    def test_syo_maukkaasti_kortilla_liian_vahan_rahaa(self):
        pal = self.kassa.syo_maukkaasti_kortilla(self.koyha_kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(pal, False)
        self.assertEqual(self.koyha_kortti.saldo, 10)

    def test_rahan_lataus_toimii(self):
        self.kassa.lataa_rahaa_kortille(self.koyha_kortti, 2000)
        self.assertEqual(self.koyha_kortti.saldo, 2010)
        self.assertEqual(self.kassa.kassassa_rahaa, 102000)

    def test_negatiivisen_summan_lataus(self):
        self.kassa.lataa_rahaa_kortille(self.koyha_kortti, -2000)
        self.assertEqual(self.koyha_kortti.saldo, 10)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
