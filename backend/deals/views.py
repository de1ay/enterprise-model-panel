from .models import Deal
from .serializers import DealSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import Http404 
from rest_framework import status

class DealsAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        deals = Deal.objects.all()
        deals_serializer = DealSerializer(deals, many=True)
        return Response(deals_serializer.data)

    def post(self, request, format=None):
        deal_serializer = DealSerializer(data=request.data)
        if deal_serializer.is_valid():
            deal_serializer.save()
            return Response(deal_serializer.data, status=status.HTTP_201_CREATED)
        return Response(deal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DealAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get_object(self, id):
        try:
            return Deal.objects.get(deal_id=id)
        except Deal.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        deal = self.get_object(id)
        deal_serializer = DealSerializer(deal)
        return Response(deal_serializer.data)

    def put(self, request, id, format=None):
        deal = self.get_object(id)
        deal_serializer = DealSerializer(deal, data=request.data)
        if deal_serializer.is_valid():
            new_deal = deal_serializer.save()
            new_deal.update_status()
            new_deal.save()
            return Response(deal_serializer.data)
        return Response(deal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        deal = self.get_object(id)
        deal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)