# from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import  serializers, status
from jayceesapi.models import Flavor

class FlavorView(ViewSet):
    """Level up flavor view"""
    def retrieve(self, request, pk):
        """Handle GET requests for single flavor

        Returns:
            Response -- JSON serialized flavor
        """
        flavor = Flavor.objects.get(pk=pk)
        serializer = FlavorSerializer(flavor)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all flavor

        Returns:
            Response -- JSON serialized list of flavor
        """
        flavors = Flavor.objects.all()
        serializer = FlavorSerializer(flavors, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle a POST request for a flavor """
        # incoming_user = request.auth.user
        flavor = Flavor.objects.create(
            flavor=request.data["flavor"],
            price=request.data["price"],
        )
        serializer = FlavorSerializer(flavor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """
        flavor = Flavor.objects.get(pk=pk)

        flavor.flavor = request.data["flavor"]
        flavor.price = request.data["price"]

        flavor.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handles a DELETE request for a flavor """
        try:
            flavor = Flavor.objects.get(pk=pk)
            flavor.delete()
        except Flavor.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class FlavorSerializer(serializers.ModelSerializer):
    """JSON serializer for flavor
    """
    class Meta:
        model = Flavor
        fields = ('id', 'flavor', 'price')

# class CreateFlavorSerializer(serializers.ModelSerializer):
#     """JSON serializer for flavor
#     """
#     class Meta:
#         model = Flavor
#         fields = ('id', 'flavor', 'price')
