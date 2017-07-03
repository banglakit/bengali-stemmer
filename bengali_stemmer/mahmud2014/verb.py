# coding: utf-8
import logging

logger = logging.getLogger(__name__)


def _stem_verb_step_1(word: str) -> str:
    if word.endswith(('ই', 'ছ', 'ত', 'ব', 'ল', 'ন', 'ক', 'স', 'ম')):
        return word[:-1]
    return word


def _stem_verb_step_2(word: str) -> str:
    if word.endswith(('লা', 'তা', 'ছি', 'বে', 'তে', 'ছে', 'লে')):
        return word[:-2]
    return word


def _stem_verb_step_3(word: str) -> str:
    if word.endswith(('ছি', 'ছে')):
        return word[:-2]
    return word


def _harmonize_verb(word: str) -> str:
    logger.warning('Harmonizing has not been implemented completely.')
    if word.endswith('য়ে'):
        return word[:-3] + 'ে'
    if word.endswith('ই'):
        return word[:-2] + 'া'
    return word


def _stem_verb_step_4(word: str) -> str:
    if len(word) > 1 and not word.endswith(('ই', 'য়ে', 'ও')):
        if word.endswith(('া', 'ে', 'ি')):
            return word[:-1]
        return word
    else:
        return _harmonize_verb(word)


def stem_verb(word: str) -> str:
    stemmed = _stem_verb_step_1(word)
    stemmed = _stem_verb_step_2(stemmed)
    stemmed = _stem_verb_step_3(stemmed)
    stemmed = _stem_verb_step_4(stemmed)
    return stemmed
