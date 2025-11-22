from expects import expect, equal, raise_error
from cesar import cesar_encrypt

class TestChiffrementCesar:
    """Tester la fonctionnalité de chiffrement."""
    
    def test_chiffrement_basique_minuscules(self):
        resultat = cesar_encrypt("abc", 3)
        expect(resultat).to(equal("def"))
    
    def test_chiffrement_basique_majuscules(self):
        resultat = cesar_encrypt("ABC", 3)
        expect(resultat).to(equal("DEF"))
    
    def test_chiffrement_mixte(self):
        resultat = cesar_encrypt("Hello", 3)
        expect(resultat).to(equal("Khoor"))
    
    def test_decalage_boucle_minuscules(self):
        resultat = cesar_encrypt("xyz", 3)
        expect(resultat).to(equal("abc"))
    
    def test_decalage_boucle_majuscules(self):
        resultat = cesar_encrypt("XYZ", 3)
        expect(resultat).to(equal("ABC"))
    
    def test_preserve_espaces(self):
        resultat = cesar_encrypt("hello world", 3)
        expect(resultat).to(equal("khoor zruog"))
    
    def test_preserve_ponctuation(self):
        resultat = cesar_encrypt("hello, world!", 3)
        expect(resultat).to(equal("khoor, zruog!"))
    
    def test_preserve_chiffres(self):
        resultat = cesar_encrypt("test123", 3)
        expect(resultat).to(equal("whvw123"))
    
    def test_decalage_zero(self):
        resultat = cesar_encrypt("hello", 0)
        expect(resultat).to(equal("hello"))
    
    def test_decalage_negatif(self):
        resultat = cesar_encrypt("def", -3)
        expect(resultat).to(equal("abc"))
    
    def test_decalage_grand(self):
        resultat = cesar_encrypt("abc", 29)  # 29 % 26 = 3
        expect(resultat).to(equal("def"))
    
    def test_chaine_vide(self):
        resultat = cesar_encrypt("", 3)
        expect(resultat).to(equal(""))
    
    def test_caracteres_speciaux_uniquement(self):
        resultat = cesar_encrypt("!@#$%", 3)
        expect(resultat).to(equal("!@#$%"))
    
    def test_type_texte_invalide(self):
        expect(lambda: cesar_encrypt(123, 3)).to(raise_error(TypeError, "Le texte entré doit être une chaîne de caractères"))
    
    def test_type_decalage_invalide(self):
        expect(lambda: cesar_encrypt("abc", "3")).to(raise_error(TypeError, "Le décalage doit être un entier"))
