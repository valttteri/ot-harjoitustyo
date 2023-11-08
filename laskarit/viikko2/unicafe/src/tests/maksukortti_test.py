import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 11.0)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_saldoa_ei_voi_ylittaa(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_ota_rahaa_palauttaa_oikean_totuusarvon(self):
        self.assertTrue(self.maksukortti.ota_rahaa(600))
        self.assertFalse(self.maksukortti.ota_rahaa(1100))