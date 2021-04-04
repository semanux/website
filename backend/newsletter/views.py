from newsletter.models import Subscriber
from newsletter.serializers import SubscriberSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.parsers import JSONParser
from rest_framework import mixins
from rest_framework import generics

from rest_framework import viewsets
from rest_framework import permissions


class SubscriberList(APIView):
    """
    List all subscribers, or create a new subscriber.
    """
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #data = JSONParser().parse(request)
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscriberDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a subscriber.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SubscriberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Subscriber to be viewed or edited.
    """
    queryset = Subscriber.objects.all().order_by('-created')
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.IsAuthenticated]