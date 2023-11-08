import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_konstruktorin_toiminta(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_valid(self):
        tapahtuma = self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(tapahtuma, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_invalid(self):
        tapahtuma = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(tapahtuma, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_valid(self):
        tapahtuma = self.kassapaate.syo_maukkaasti_kateisella(450)

        self.assertEqual(tapahtuma, 50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_invalid(self):
        tapahtuma = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(tapahtuma, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_valid(self):
        tapahtuma = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertTrue(tapahtuma)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.maksukortti.saldo, 760)
    
    def test_syo_edullisesti_kortilla_invalid(self):
        kortti = Maksukortti(200)
        tapahtuma = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertFalse(tapahtuma)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(kortti.saldo, 200)
    
    def test_syo_maukkaasti_kortilla_valid(self):
        tapahtuma = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertTrue(tapahtuma)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.maksukortti.saldo, 600)
    
    def test_syo_maukkaasti_kortilla_invalid(self):
        kortti = Maksukortti(300)
        tapahtuma = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertFalse(tapahtuma)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(kortti.saldo, 300)
    
    def test_lataa_rahaa_kortille_valid(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        
        self.assertEqual(self.maksukortti.saldo, 1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
    
    def test_lataa_rahaa_kortille_invalid(self):
        tapahtuma = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)

        self.assertIsNone(tapahtuma)
        self.assertEqual(self.maksukortti.saldo, 1000)  
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
    
