import pytest

from lessons.lesson3.classwork import acronym, anagram, rotational_cipher
from lessons.lesson3.tests.models import AcronymTestData, AnagramTestData, CesarTestData

acronym_data = [
    AcronymTestData(sentence="National Auto Sport Association", answer="NASA"),
    AcronymTestData(sentence="Protocol School of Washington", answer="PSOW"),
    AcronymTestData(sentence="xtreme fight championship", answer="XFC"),
]

anagram_data = [
    AnagramTestData(
        word="python",
        candidates=["pytnoh", "yoga", "yohnpt", "pyton", "pypy"],
        answer=["pytnoh", "yohnpt"],
    ),
    AnagramTestData(
        word="incomprehensibilities",
        candidates=[
            "roblshiepicineeimist",
            "initnieprlhbcsiemesoi",
            "esihciltmrpeeinibson",
        ],
        answer=["initnieprlhbcsiemesoi"],
    ),
    AnagramTestData(
        word="sesquipedalianism",
        candidates=[
            "snuimsaielaqqdpei",
            "sqeeausisimpiland",
            "uilenmiqaeiadssss",
        ],
        answer=["sqeeausisimpiland"],
    ),
]

cipher_data = [
    CesarTestData(
        command="ROT11 Knowing what must be done does away with fear",
        answer="vyzhtyr hsle xfde mp ozyp ozpd lhlj htes qplc",
    ),
    CesarTestData(
        command="ROT22 A journey of a thousand miles begins with a single step",
        answer="w fkqnjau kb w pdkqowjz iehao xacejo sepd w oejcha opal",
    ),
    CesarTestData(
        command="ROT444 Many receive advice only the wise profit from it",
        answer="ocpa tgegkxg cfxkeg qpna vjg ykug rtqhkv htqo kv",
    ),
    CesarTestData(
        command="ROT13 abcdefghijklmnopqrstuvwxyz",
        answer="nopqrstuvwxyzabcdefghijklm",
    ),
]


@pytest.mark.parametrize("test_data", acronym_data)
def test_acronym(test_data: AcronymTestData):
    """Test acronym function."""
    answer = acronym(sentence=test_data.sentence)
    assert answer == test_data.answer


@pytest.mark.parametrize("test_data", anagram_data)
def test_anagram(test_data: AnagramTestData):
    """Test anagram function."""
    answer = anagram(word=test_data.word, candidates=test_data.candidates)
    assert answer == test_data.answer


@pytest.mark.parametrize("test_data", cipher_data)
def test_cipher(test_data: CesarTestData):
    """Test rotational_cipher function."""
    answer = rotational_cipher(command=test_data.command)
    assert answer == test_data.answer
