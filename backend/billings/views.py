from .models import Billing
from .serializers import BillingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import Http404
from rest_framework import status


class BillingsAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        billing = Billing.objects.all()
        billing_serializer = BillingSerializer(billing, many=True)
        return Response(billing_serializer.data)

    def post(self, request, format=None):
        billing_serializer = BillingSerializer(data=request.data)
        if billing_serializer.is_valid():
            billing = billing_serializer.save()
            related_deal = billing.billing_deal
            related_deal.change_paid_value(billing.billing_sum)
            return Response(billing_serializer.data, status=status.HTTP_201_CREATED)
        return Response(billing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillingAPI(APIView):

    renderer_classes = (JSONRenderer, )

    def get_object(self, id):
        try:
            return Billing.objects.get(billing_id=id)
        except Billing.DoesNotExist:
            return Http404

    def get(self, request, id, format=None):
        billing = self.get_object(id)
        billing_serializer = BillingSerializer(billing)
        return Response(billing_serializer.data)

    def put(self, request, id, format=None):
        billing = self.get_object(id)
        billing_serializer = BillingSerializer(billing, data=request.data)
        if billing_serializer.is_valid():
            new_billing = billing_serializer.save()
            related_deal = billing.billing_deal
            related_deal.change_paid_value(new_billing.billing_sum - billing.billing_sum)
            return Response(billing_serializer.data)
        return Response(billing_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        billing = self.get_object(id)
        related_deal = billing.billing_deal
        related_deal.change_paid_value(billing.billing_sum * -1)
        billing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)