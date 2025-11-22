from expects import expect, equal, contain
from cesar import cesar_encrypt, cesar_crack


class TestCassageCesar:
    """Tester la fonctionnalité de cassage par force brute."""
    
    def test_cassage_retourne_tous_les_decalages(self):
        chiffre = "def"
        resultats = cesar_crack(chiffre)
        expect(len(resultats)).to(equal(26))
    
    def test_cassage_contient_original(self):
        original = "hello"
        chiffre = cesar_encrypt(original, 7)
        resultats = cesar_crack(chiffre)
        expect(resultats).to(contain(original))
    
    def test_cassage_decalage_3(self):
        chiffre = "khoor"
        resultats = cesar_crack(chiffre)
        expect(resultats[3]).to(equal("hello"))