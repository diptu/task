from rest_framework.generics import ListAPIView, RetrieveAPIView
from subscription.models import Subscription
from rest_framework import views
from .serializers import SubscriptionSerializer , JoinVSChannelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db import connection
class SubscriptionListView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionDetailView(RetrieveAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

# class JoinVSChannelView(ModelViewSet):
#     # The usual stuff here
#     model = Subscription
#     queryset = Subscription.objects.all()

#     def list(self, request):
#         queryset = Subscription.objects.raw("""
#         					select id,
#                 	 		extract(EPOCH from TO_TIMESTAMP(subscription_on, 'DD-MM-YYYY HH24:MI:SS.US')),
#                 	 		retailer_type
#                 			FROM public.subscription_data
#                 			where current_product_code='TonicBasic' and retailer_type is not null
#                             group by retailer_type,id
#                 			limit 10;""")
        
#         serializer = JoinVSChannelSerializer(queryset, many=True)
        
#         return Response(serializer.data)


class JoinVSChannelView(views.APIView):

    def get(self, request):
        queryset= Subscription.objects.raw("""
                          select id,
                          extract(MONTH from TO_TIMESTAMP(subscription_on, 'DD-MM-YYYY HH24:MI:SS.US')),
                          retailer_type as retailer
                          FROM public.subscription_data
                          where current_product_code='TonicBasic' and retailer_type is not null
                            group by retailer_type,id
                          limit 10;""")
        results = JoinVSChannelSerializer(queryset, many=True).data
        return Response(results)

