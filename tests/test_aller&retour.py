from expects import expect, equal
from cesar import cesar_encrypt, cesar_decrypt, cesar_crack

class TestAllerRetourCesar:
    """Tester que chiffrement et déchiffrement sont inverses."""
    
    def test_aller_retour_decalage_1(self):
        original = "hello"
        chiffre = cesar_encrypt(original, 1)
        dechiffre = cesar_decrypt(chiffre, 1)
        expect(dechiffre).to(equal(original))
    
    def test_aller_retour_decalage_13(self):
        original = "The quick brown fox"
        chiffre = cesar_encrypt(original, 13)
        dechiffre = cesar_decrypt(chiffre, 13)
        expect(dechiffre).to(equal(original))
    
    def test_aller_retour_decalage_25(self):
        original = "ABCXYZ"
        chiffre = cesar_encrypt(original, 25)
        dechiffre = cesar_decrypt(chiffre, 25)
        expect(dechiffre).to(equal(original))
    
    def test_aller_retour_texte_complexe(self):
        original = "Hello, World! 123 Testing..."
        for decalage in range(1, 26):
            chiffre = cesar_encrypt(original, decalage)
            dechiffre = cesar_decrypt(chiffre, decalage)
            expect(dechiffre).to(equal(original))