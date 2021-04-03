from rest_framework import serializers
from newsletter.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ('id','created', 'email', 'flag')

