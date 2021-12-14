from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from giftbuddyapi.models import Interest
from giftbuddyapi.models import Gifter

class InterestView(ViewSet):
    """GIft Buddy Interests"""
    def create(self, request):
        """"""
        gifter = Gifter.objects.get(user=request.auth.user)
        try:
            interest = Interest.objects.create(
                label=request.data["label"]
            )
            serializer = InterestSerializer(interest, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single interest

        Returns:
            Response -- JSON serialized interest
        """
        try:
            interest = Interest.objects.get(pk=pk)
            serializer = InterestSerializer(interest, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """"""
        interests = Interest.objects.all()
        serializer = InterestSerializer(
            interests, many=True, context={'request': request})
        return Response(serializer.data)
        


class InterestSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Interest
        fields = ('id', 'label')