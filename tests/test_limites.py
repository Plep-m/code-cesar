from expects import expect, equal, raise_error
from cesar import cesar_encrypt

class TestCasLimitesCesar:
    """Tester les cas limites et la gestion des erreurs."""
    
    def test_un_seul_caractere(self):
        resultat = cesar_encrypt("a", 1)
        expect(resultat).to(equal("b"))
    
    def test_tout_majuscules(self):
        resultat = cesar_encrypt("HELLO WORLD", 5)
        expect(resultat).to(equal("MJQQT BTWQI"))
    
    def test_tout_minuscules(self):
        resultat = cesar_encrypt("hello world", 5)
        expect(resultat).to(equal("mjqqt btwqi"))
    
    def test_melange(self):
        resultat = cesar_encrypt("heLLO WOrld", 5)
        expect(resultat).to(equal("mjQQT BTwqi"))
    
    def test_caracteres_unicode_inchanges(self):
        resultat = cesar_encrypt("café", 3)
        expect(resultat).to(equal("fdié"))
    
    def test_type_texte_invalide(self):
        expect(lambda: cesar_encrypt(123, 3)).to(raise_error(TypeError))
    
    def test_type_decalage_invalide(self):
        expect(lambda: cesar_encrypt("hello", "3")).to(raise_error(TypeError))
    
    def test_texte_tres_long(self):
        texte_long = "a" * 10000
        resultat = cesar_encrypt(texte_long, 1)
        expect(len(resultat)).to(equal(10000))
        expect(resultat).to(equal("b" * 10000))