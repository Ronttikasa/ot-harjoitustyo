import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    # kortin saldo alussa oikein
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    #rahan lataaminen kasvattaa saldoa oikein
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1990)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    #saldo vähenee oikein jos rahaa on tarpeeksi
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.lataa_rahaa(1990)
        self.maksukortti.ota_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")    

    #saldo ei muutu jos rahaa ei ole tarpeeksi
    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    #jos rahat riittivät, metodi palauttaa True ja muuten False
    def test_ota_rahaa_kertoo_riittivatko_rahat(self):
        palautus = self.maksukortti.ota_rahaa(5)
        self.assertEqual(palautus, True)

    def test_otar_rahaa_kertoo_riittivatko_rahat2(self):
        palautus = self.maksukortti.ota_rahaa(100)
        self.assertEqual(palautus, False)