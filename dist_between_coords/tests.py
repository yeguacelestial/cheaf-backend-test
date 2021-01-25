from django.test import TestCase


class DistBetweenCordsTest(TestCase):

    def test_can_calculate_distance_between_coords(self):
        """
            Can calculate dist between two different geo-coords.
        """
        coords = {
            "coords": [
                {
                    "lat": 52.12212,
                    "long": 12.12312
                },
                {
                    "lat": 23.2313,
                    "long": 23.23123
                }
            ]
        }

        expected_response = {
            'dist_km': 3344.3756516279086,
            'dist_miles': 2078.0986859415443
        }

        response = self.client.post('/api/v1/dist-between-coords/', coords)
        self.assertEqual(response.data, expected_response)

    def test_send_invalid_request(self):
        """
            Send an invalid request with wrong parameters.
        """
        coords = {
            'coords': [
                {
                    'coord1': {
                        'lat': 52.12212,
                        'long': 12.12312
                    }
                },
            ]
        }

        expected_response = {
            'error': 'Invalid request',
            'message': 'This endpoint requires 2 coordinates, with lat-long values.'
        }

        response = self.client.post('/api/v1/dist-between-coords/', coords)
        self.assertEqual(response.data, expected_response)
