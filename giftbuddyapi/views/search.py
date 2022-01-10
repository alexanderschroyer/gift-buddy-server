from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import requests


class SearchView(ViewSet):
    """
    """
    def list(self, request):
        """Handle GET requests to recipients resource

        Returns:
            Response -- JSON serialized list of recipients
        """
        query = self.request.query_params.get('q', None)
        results = requests.get(f"https://serpapi.com/search.json?engine=google&location=Tuscaloosa&tbm=shop&location=&q={query}&api_key=8b3c15f839a5418a9b8d4b7085066b273350a46a1297df1cc67da153043939d9")

        return Response(results.json())