from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework import viewsets
from rest_framework import permissions

from newsletter.models import Subscriber
from newsletter.serializers import SubscriberSerializer

import json

@csrf_exempt
def subscriber(request):
	"""
	List all log records, or create a new log.
	"""
	if request.method == 'GET':
		subs = Subscriber.objects.all()
		serializer = SubscriberSerializer(subs, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		#data['user'] = USER
		serializer = SubscriberSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


class SubscriberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Subscriber to be viewed or edited.
    """
    queryset = Subscriber.objects.all().order_by('-created')
    serializer_class = SubscriberSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def subscriber_detail(request, pk):
    """
    Retrieve, update or delete a subscriber.
    """
    try:
        sub = Subscriber.objects.get(pk=pk)
    except Subscriber.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SubscriberSerializer(sub)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubscriberSerializer(sub, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        sub.delete()
        return HttpResponse(status=204)
