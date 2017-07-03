from unittest import TestCase


class TestTestCase(TestCase):
    def test_mahmud_basic(self):
        from bengali_stemmer.mahmud2014 import stem_verb
        self.assertEqual(stem_verb('পড়ছিলাম'), 'পড়')
