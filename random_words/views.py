from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from .serializers import RandomWordsSerializer


class RandomWords(APIView):
    """
        View to send a list of 10 random words.
    """

    def post(self, request):
        """
            Sends a list of 10 random words. Returns a list with the words, and
            the number of times they appear in the list.
        """
        my_serializer = RandomWordsSerializer(data=request.data)

        if my_serializer.is_valid():
            # Get list of words on the request
            word_list = my_serializer.data['words']

            response = []
            passed_words = []  # This list saves the words already saved

            for word in word_list:
                if word not in passed_words:
                    response.append({word: word_list.count(word)})
                    passed_words.append(word)

            status_code = status.HTTP_200_OK

        else:
            response = {
                'error': 'Invalid request.',
                'message': "Number of words required: 10."
            }
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(response, status_code)
