#from django.http import JsonResponse
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view


from complaints.models import Complaint
from complaints.serializers import ComplaintSerializer


@api_view(["POST", "GET"])
def api_home(request, *argss, **kwargs):
    serializer = ComplaintSerializer(data = request.data)
    if serializer.is_valid(raise_exception = True):
        """instance = Complaint.objects.all().order_by("?")[0]
        data = {}
        if instance:
            data = ComplaintSerializer(instance).data
        return Response(data)"""
        data = serializer.data
        return Response(data=data)
