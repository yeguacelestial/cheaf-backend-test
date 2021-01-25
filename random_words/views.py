from rest_framework.views import APIView
from rest_framework.response import Response

import json

class RandomWords(APIView):
    """
        View to send a list of 10 random words.
    """

    def post(self, request):
        """
            Sends a list of 10 random words. Returns a list with the words, and
            the number of times they appear in the list.
        """
        # print(request.data)
        return Response({'hello':'world'})