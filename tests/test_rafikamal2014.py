from bengali_stemmer.rafikamal2014.parser import RafiStemmerRuleParser
from bengali_stemmer.rafikamal2014.parser import RafiStemmer

DUMMY_RULES = """{
\tই\t\t\t# এটাই, সেটাই
\tও\t\t\t# এটাও, সেটাও
\tতো\t\t\t# হয়তো, করলতো
}

{
\tকে\t\t\t# এটাকে, আমাকে
\tতে\t\t\t# হাসতে, গাইতে
\tরা\t\t\t# রহিমরা, করিমরা
}"""


class TestFileParser:
    def test_remove_whitespace(self):
        parser = RafiStemmerRuleParser(DUMMY_RULES)

        assert parser.remove_whitespace('a -> b') == 'a->b'
        assert parser.remove_whitespace('a ->\tb') == 'a->b'
        assert parser.remove_whitespace('a\t->\tb') == 'a->b'
        assert parser.remove_whitespace('a\t\t->\tb') == 'a->b'

    def test_remove_comments(self):
        parser = RafiStemmerRuleParser(DUMMY_RULES)

        assert parser.remove_comments('a -> b # this is not it') == 'a -> b '
        assert parser.remove_comments('') == ''
        assert parser.remove_comments('a -> b') == 'a -> b'
        assert parser.remove_comments('# moyna go') == ''

    def test_extract_replace_rule(self):
        parser = RafiStemmerRuleParser(DUMMY_RULES)

        assert parser.extract_replace_rule('a->b') == 'b'
        assert parser.extract_replace_rule('a') is None
        assert parser.extract_replace_rule('') is None

    def test_group_rules(self):
        parser = RafiStemmerRuleParser(DUMMY_RULES)

        assert parser.groups == [['ই', 'ও', 'তো'], ['কে', 'তে', 'রা']]


class TestStemmer:
    def test_random_sample(self):
        parser = RafiStemmer()

        assert parser.stem_word("আমি") == 'আমি'
        assert parser.stem_word("বাংলায়") == 'বাংলা'
        assert parser.stem_word("গান") == 'গান'
        assert parser.stem_word("গাই") == 'গা'
        assert parser.stem_word("ভাতের") == 'ভাত'
