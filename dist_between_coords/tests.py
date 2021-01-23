from django.test import TestCase


class DistBetweenCordsTest(TestCase):

    def test_can_calculate_distance_between_coords(self):
        """
            Can calculate dist between two different geo-coords.
        """
        self.assertEqual('coord1', 'coord2')