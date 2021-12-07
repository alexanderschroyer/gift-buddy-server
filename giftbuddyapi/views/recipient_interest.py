from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from giftbuddyapi.models import RecipientInterest
from giftbuddyapi.views.recipient import RecipientInterestSerializer

class RecipientInterest(ViewSet):
    """"""

    def retrieve(self, request, pk=None):
        """"""
        try:
            recipient_interest = RecipientInterest.objects.get(pk=pk)
            serializer = RecipientInterestSerializer(recipient_interest, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """"""
        recipient_interests = RecipientInterest.objects.all()

        serializer = RecipientInterestSerializer(
            recipient_interests, many=True, context={'request': request})
        return Response(serializer.data)