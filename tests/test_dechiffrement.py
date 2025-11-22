from expects import expect, equal
from cesar import cesar_encrypt, cesar_decrypt

class TestDechiffrementCesar:
    """Tester la fonctionnalité de déchiffrement."""
    
    def test_dechiffrement_basique(self):
        resultat = cesar_decrypt("def", 3)
        expect(resultat).to(equal("abc"))
    
    def test_dechiffrement_majuscules(self):
        resultat = cesar_decrypt("DEF", 3)
        expect(resultat).to(equal("ABC"))
    
    def test_dechiffrement_mixte(self):
        resultat = cesar_decrypt("Khoor", 3)
        expect(resultat).to(equal("Hello"))
    
    def test_dechiffrement_avec_espaces(self):
        resultat = cesar_decrypt("khoor zruog", 3)
        expect(resultat).to(equal("hello world"))
    
    def test_dechiffrement_avec_ponctuation(self):
        resultat = cesar_decrypt("khoor, zruog!", 3)
        expect(resultat).to(equal("hello, world!"))
    
    def test_chiffrement_puis_dechiffrement(self):
        original = "The quick brown fox jumps over the lazy dog"
        chiffre = cesar_encrypt(original, 13)
        dechiffre = cesar_decrypt(chiffre, 13)
        expect(dechiffre).to(equal(original))
