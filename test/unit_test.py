from src.word_model import WordModel


def test_valid_original_word():
    word = WordModel('example')
    assert word.original == 'example'


def test_valid_reversed_word():
    word = WordModel('example')
    assert word.reversed == 'elpmaxe'
