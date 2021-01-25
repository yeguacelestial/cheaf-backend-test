import json

from geopy.distance import distance
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DistBetweenCoordsSerializer


class DistBetweenCoords(APIView):
    """
        View to send two coordinates, and know the distance between them.
    """

    def post(self, request):
        """
            Sends a dict of two coordinates, with lat-long parameters.
            Returns a dict with the distance in km and miles.
        """
        coords_serializer = DistBetweenCoordsSerializer(data=request.data)

        if coords_serializer.is_valid():
            coords = coords_serializer.data['coords']

            # If it's necessary, convert JSON string to dictionary
            try:
                coords = [coord.replace("'", '"') for coord in coords]
                coords = [json.loads(coord) for coord in coords]

            except AttributeError:
                pass
            
            # Try to get lat-long values for coordinates
            try:
                lat1 = coords[0]['lat']
                long1 = coords[0]['long']
                coord1 = (lat1, long1)

                lat2 = coords[1]['lat']
                long2 = coords[1]['long']
                coord2 = (lat2, long2)

                dist_km = distance(coord1, coord2).km
                dist_miles = distance(coord1, coord2).miles

                response = {
                    "dist_km": dist_km,
                    "dist_miles": dist_miles
                }

                status_code = status.HTTP_200_OK

                return Response(response, status_code)

            except:
                response = {
                    'error': 'Invalid request',
                    'message': 'This endpoint requires 2 coordinates, with lat-long values.'
                }
                status_code = status.HTTP_400_BAD_REQUEST

        else:
            response = {
                'error': 'Invalid request',
                'message': 'This endpoint requires 2 coordinates, with lat-long values.'
            }
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(response, status_code)