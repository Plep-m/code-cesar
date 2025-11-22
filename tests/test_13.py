from expects import expect, equal
from cesar import cesar_encrypt

class Test13Cesar:
    """Tester spécifiquement 13 (décalage de 13)."""
    
    def test_13_basique(self):
        resultat = cesar_encrypt("hello", 13)
        expect(resultat).to(equal("uryyb"))
    
    def test_13_inversible(self):
        original = "The quick brown fox"
        chiffre = cesar_encrypt(original, 13)
        dechiffre = cesar_encrypt(chiffre, 13)
        expect(dechiffre).to(equal(original))
    
    def test_13_preserve_casse(self):
        resultat = cesar_encrypt("HeLLo", 13)
        expect(resultat).to(equal("UrYYb"))