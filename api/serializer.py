from rest_framework import serializers
from .models import MyApiModel

class MySerializer(serializers.ModelSerializer):#ModelSerializer is a base class for the DataSerializer
    eid=serializers.IntegerField(label=("enter the eid:-"),required=True,style={"input_type":"text","autofocus":False,"autocomplete":"off","required":True},error_messages={"required":"thisfield is required","blank":"eid is required.",},)
    name=serializers.CharField(max_length=50)
    class1=serializers.CharField(max_length=20)
    email=serializers.EmailField(max_length=80)
    class Meta:
        model=MyApiModel
        fields=('eid','name','class1','email')
        
        