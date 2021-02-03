from dataclasses import dataclass
from typing import List


@dataclass
class AcronymTestData:
    """Test data for acronym function."""

    sentence: str
    answer: str


@dataclass
class AnagramTestData:
    """Test data for anagram function."""

    word: str
    candidates: List[str]
    answer: List[str]


@dataclass
class CesarTestData:
    """Test data for Cesar cipher."""

    command: str
    answer: str
