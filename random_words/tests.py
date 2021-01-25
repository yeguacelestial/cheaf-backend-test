from rest_framework.test import APITestCase


class RandomWordsTest(APITestCase):

    def test_send_random_words(self):
        """
            Can send a list of random words, and can return the number of times
            those appear on the list.
        """
        words = {
            "words": [
                "prescription",
                "capture",
                "impress",
                "cheat",
                "capture",
                "impress",
                "plaintiff",
                "partner",
                "impress",
                "partner",
            ]
        }

        expected_response = [
            {"prescription":1},
            {"capture":2},
            {"impress":3},
            {"cheat":1},
            {"plaintiff":1},
            {"partner":2},
        ]

        response = self.client.post('/api/v1/random-words/', words)
        self.assertEqual(response.data, expected_response)

    def test_send_less_than_ten_words(self):
        """
            Sends less than 10 words, and evaluates the response.
        """
        words = {
            "words": [
                "prescription",
                "capture",
                "impress",
            ]
        }

        expected_response = {
            "error": "Invalid request.",
            "message": "Number of words required: 10."
        }

        response = self.client.post('/api/v1/random-words/', words)
        self.assertEqual(response.data, expected_response)

    def test_send_more_than_ten_words(self):
        """
            Sends more than 10 words, and evaluates the response.
        """
        words = {
            "words": [
                "prescription",
                "capture",
                "impress",
                "impress",
                "cheat",
                "capture",
                "impress",
                "plaintiff",
                "partner",
                "impress",
                "partner",
            ]
        }

        expected_response = {
            "error": "Invalid request.",
            "message": "Number of words required: 10."
        }

        response = self.client.post('/api/v1/random-words/', words)
        self.assertEqual(response.data, expected_response)
