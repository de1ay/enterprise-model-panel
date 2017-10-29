from .models import Client
from .serializers import ClientSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import Http404 
from rest_framework import status

class ClientsAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        client = Client.objects.all()
        client_serializer = ClientSerializer(client, many=True)
        return Response(client_serializer.data)

    def post(self, request, format=None):
        client_serializer = ClientSerializer(data=request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(client_serializer.data, status=status.HTTP_201_CREATED)
        return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get_object(self, id):
        try:
            return Client.objects.get(client_id=id)
        except Client.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        client = self.get_object(id)
        client_serializer = ClientSerializer(client)
        return Response(client_serializer.data)

    def put(self, request, id, format=None):
        client = self.get_object(id)
        client_serializer = ClientSerializer(client, data=request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(client_serializer.data)
        return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        client = self.get_object(id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)