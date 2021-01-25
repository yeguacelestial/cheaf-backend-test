from rest_framework import status
from rest_framework.test import APITestCase

import json


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
                "partner"
            ]
        }

        expected_response = [
            {"prescription":"1"},
            {"capture":"2"},
            {"impress":"3"},
            {"cheat":"1"},
            {"plaintiff":"1"},
            {"partner":"2"},
        ]
        response = self.client.post('/api/v1/random-words/', words)

        self.assertEqual(expected_response, response.data)