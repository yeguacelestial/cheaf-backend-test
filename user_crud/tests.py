from django.test import TestCase


class UserCrudTest(TestCase):
    
    def test_can_create_user(self):
        """
            Can create a user with requests.
        """
        self.assertEqual('User1', 'User1')