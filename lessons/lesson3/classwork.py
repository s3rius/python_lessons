from typing import List


def acronym(sentence: str) -> str:
    """
    Convert a phrase to its acronym.

    Techies love their TLA (Three Letter Acronyms)!
    Help generate some jargon by writing a program that converts
    a long name to its acronym.

    Example:
    >>> result = acronym("Portable Network Graphics")
    >>> assert result == "PNG"

    :param sentence: Sentence with more than one word.
    :return: sentence's acronym.
    """
    return ""


def anagram(word: str, candidates: List[str]) -> List[str]:
    """
    Find possible anagrams.

    An anagram is a rearrangement of letters to form a new word.
    Given a word and a list of candidates,
    select the sublist of anagrams of the given word.

    Example:
    >>> answer = anagram("listen", ["enlists" "google" "inlets" "banana"])
    >>> assert answer == ["inlets"]


    :param word: target word with length > 0.
    :param candidates: possible candidates.
    :return: List of anagrams
    """
    return []


def rotational_cipher(command: str) -> str:
    """
    Caesar cipher.

    Create an implementation of the rotational cipher,
    also sometimes called the Caesar cipher.

    The Caesar cipher is a simple shift cipher that relies
    on transposing all the letters in the alphabet using an integer key
    between 0 and 26. Using a key of 0 or 26 will always yield the
    same output due to modular arithmetic.
    The letter is shifted for as many values as the value of the key.

    The general notation for rotational ciphers is ROT + <key>.
    The most commonly used rotational cipher is ROT13.

    Example:
    >>> rotation = rotational_cipher("ROT13 abcdefghijklmnopqrstuvwxyz")
    >>> assert rotation == "nopqrstuvwxyzabcdefghijklm"

    :param command: rotation command with ROT index > 0.
    :return: cipher
    """
    return ""
