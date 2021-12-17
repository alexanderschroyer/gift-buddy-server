from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from giftbuddyapi.models import Gifter
from django.contrib.auth.models import User

class GifterView(ViewSet):
    """"""
    @action(methods=['get'], detail=False)
    def currentuser(self, request):
        """"""
        gifter = Gifter.objects.get(user=request.auth.user)
        try:
            serializer = GifterSerializer(gifter, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Gifter.DoesNotExist:
            return Response(
                [], status=status.HTTP_204_NO_CONTENT
            )

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users on authors on posts"""
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username' )

class GifterSerializer(serializers.ModelSerializer):
    """JSON serializer for gifters

    Arguments:
        serializer type
    """
    user = UserSerializer()
    class Meta:
        model = Gifter
        fields = ('id', 'user')