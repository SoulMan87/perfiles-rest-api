from rest_framework.views import APIView
from rest_framework.views import Response

class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})





