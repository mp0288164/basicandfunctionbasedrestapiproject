from django.shortcuts import render
from . models import MyApiModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializer import MySerializer
# Create your views here.

@api_view(['GET'])
def getdata(request):
    sz=MyApiModel.objects.all()
    serializer=MySerializer(sz,many=True)
    return Response(serializer.data)
#post add
@api_view(['POST'])
def postdata(req):
    serializer=MySerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)