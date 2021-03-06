from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from giftbuddyapi.models import Recipient, RecipientInterest, Gifter, Interest
from django.contrib.auth.models import User


class RecipientView(ViewSet):
    """Gift Buddy recipients"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized recipient instance
        """
        gifter = Gifter.objects.get(user=request.auth.user)
        try:
            recipient = Recipient.objects.create(
                gifter=gifter,
                name=request.data["name"]
            )
            recipient.interests.set(request.data['interests'])
            serializer = RecipientSerializer(recipient, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single recipient

        Returns:
            Response -- JSON serialized recipient instance
        """
        try:
            recipient = Recipient.objects.get(pk=pk)
            serializer = RecipientSerializer(recipient, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to recipients resource

        Returns:
            Response -- JSON serialized list of recipients
        """
        recipients = Recipient.objects.all()

        recipient_interest = self.request.query_params.get('interest', None)
        # if recipient_interest in not None:
        #     recipients = recipients.filter(interest=recipient_interest)

        serializer = RecipientSerializer(
            recipients, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single recipient

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            recipient = Recipient.objects.get(pk=pk)
            recipient.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Recipient.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        """"""
        gifter = Gifter.objects.get(user=request.auth.user)

        recipient = Recipient.objects.get(pk=pk)
        recipient.gifter = gifter
        recipient.name = request.data["name"]
        recipient.interests.set(request.data['interests'])
        recipient.save()

        return Response({'hey now'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False)
    def currentuser(self, request):
        """"""
        gifter = Gifter.objects.get(user=request.auth.user)
        try:
            recipients = Recipient.objects.filter(gifter=gifter)
            serializer = RecipientSerializer(recipients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Recipient.DoesNotExist:
            return Response(
                [], status=status.HTTP_204_NO_CONTENT
            )

class RecipientUserSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

class GifterSerializer(serializers.ModelSerializer):
    """JSON serializer for gifters

    Arguments:
        serializer type
    """
    user = RecipientUserSerializer(many=False)
    class Meta:
        model = Gifter
        fields = ('id', 'user')

class InterestSerializer(serializers.ModelSerializer):
    """JSON serializer for interests

    Arguments:
        serializer type
    """ 
    class Meta:
        model = Interest
        fields = ('id','label')

class RecipientInterestSerializer(serializers.ModelSerializer):
    """JSON serializer for interests

    Arguments:
        serializer type
    """
    class Meta:
        model = RecipientInterest
        fields = ('id', 'interest')

class RecipientSerializer(serializers.ModelSerializer):
    """JSON serializer for recipients

    Arguments:
        serializer type
    """
    gifter = GifterSerializer()
    interests = InterestSerializer(many=True)
    class Meta:
        model = Recipient
        fields = ('id', 'gifter', 'name', 'interests')