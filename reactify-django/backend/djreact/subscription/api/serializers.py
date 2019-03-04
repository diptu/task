from rest_framework import serializers
from subscription.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('__all__')

# class JoinVSChannelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscription
#         #fields = ('id','subscription_on','retailer_type')
#         fields = ('subscription_on','retailer_type')



class JoinVSChannelSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   #id = serializers.IntegerField()
   subscription_on = serializers.DateTimeField()
   retailer = serializers.CharField(max_length=200)