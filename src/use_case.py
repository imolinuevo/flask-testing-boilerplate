from src.word_model import WordModel


def reverse_use_case(input_word):
    word = WordModel(input_word)
    return {'result': word.reversed}
