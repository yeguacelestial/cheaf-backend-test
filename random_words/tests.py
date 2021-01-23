from django.test import TestCase


class RandomWordsTest(TestCase):

    def test_can_generate_words(self):
        """
            Can generate random words
        """
        self.assertEqual('word1', 'word2')