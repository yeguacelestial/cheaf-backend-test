from rest_framework import status
from rest_framework.test import APITestCase


class UserCrudTest(APITestCase):
    
    def setUp(self):
        """
            Create test case instance.
        """
        data = {
            "username": "testcase",
            "email": "test@localhost.app",
            "password": "some_strong_psw",
        }
        self.client.post('/api/v1/user-crud/', data)
    
    def test_can_create_user(self):
        """
            Can create a user.
        """
        data = {
            "username": "testcase_create",
            "email": "test_create@localhost.app",
            "password": "some_strong_psw",
        }
        response = self.client.post('/api/v1/user-crud/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_can_read_user(self):
        """
            Can read a created user.
        """
        response = self.client.get('/api/v1/user-crud/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_user(self):
        """
            Can edit a created user.
        """
        data = {
            "username": "testcase_updated",
            "email": "test_updated@localhost.app",
            "password": "another_strong_psw",
        }
        response = self.client.put('/api/v1/user-crud/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_user(self):
        """
            Can delete a created user.
        """
        response = self.client.delete('/api/v1/user-crud/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
