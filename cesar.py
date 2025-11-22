"""
Module de chiffrement César

Une implémentation simple de l'algorithme de chiffrement/déchiffrement César.
"""

from typing import List


def cesar_encrypt(texte: str, decalage: int) -> str:
    """
    Chiffre un texte en utilisant le chiffrement de César avec un décalage donné.

    Args:
        texte (str): Le texte à chiffrer
        decalage (int): Le nombre de positions de décalage pour chaque lettre

    Returns:
        str: Le texte chiffré

    Raises:
        TypeError: Si texte n'est pas une chaîne ou si decalage n'est pas un entier
    """
    raise NotImplementedError("cesar_chiffrer n'est pas encore implémenté")


def cesar_decrypt(texte: str, decalage: int) -> str:
    """
    Déchiffre un texte chiffré avec l'algorithme de César en utilisant un décalage donné.

    Args:
        texte (str): Le texte à déchiffrer
        decalage (int): Le nombre de positions pour revenir en arrière

    Returns:
        str: Le texte déchiffré
    """
    raise NotImplementedError("cesar_dechiffrer n'est pas encore implémenté")


def cesar_crack(texte_chiffre: str) -> List[str]:
    """
    Essaie tous les décalages possibles et retourne une liste de textes déchiffrés.

    Args:
        texte_chiffre (str): Le texte chiffré à casser

    Returns:
        list: Une liste de 26 déchiffrements possibles (un par décalage 0-25)
    """
    raise NotImplementedError("cesar_casser n'est pas encore implémenté")
