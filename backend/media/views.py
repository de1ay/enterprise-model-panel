from .models import Media
from .serializers import MediaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import Http404 
from rest_framework import status

class MediaAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        media = Media.objects.all()
        media_serializer = MediaSerializer(media, many=True)
        return Response(media_serializer.data)

    def post(self, request, format=None):
        media_serializer = MediaSerializer(data=request.data)
        if media_serializer.is_valid():
            media_serializer.save()
            return Response(media_serializer.data, status=status.HTTP_201_CREATED)
        return Response(media_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MediaDetailedAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get_object(self, id):
        try:
            return Media.objects.get(media_id=id)
        except Media.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        media = self.get_object(id)
        media_serializer = MediaSerializer(media)
        return Response(media_serializer.data)

    def put(self, request, id, format=None):
        media = self.get_object(id)
        media_serializer = MediaSerializer(media, data=request.data)
        if media_serializer.is_valid():
            media_serializer.save()
            return Response(media_serializer.data)
        return Response(media_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        media = self.get_object(id)
        media.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)