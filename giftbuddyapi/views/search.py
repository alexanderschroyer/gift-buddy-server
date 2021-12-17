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
        results = requests.get(f"https://serpapi.com/search.json?engine=google&location=Tuscaloosa&tbm=shop&location=&q={query}&api_key=182cb978ab8751d5eaefdb9cd92a86225572b2fc62c2e8c7fe818d8fb78485bb")

        return Response(results.json())