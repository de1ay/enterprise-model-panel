from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import Http404
from rest_framework import status


class UsersAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data)

    def post(self, request, format=None):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get_object(self, id):
        try:
            return User.objects.get(user_id=id)
        except User.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        user = self.get_object(id)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    def put(self, request, id, format=None):
        user = self.get_object(id)
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)