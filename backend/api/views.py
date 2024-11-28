from django.shortcuts import render
import json
from django.forms.models import model_to_dict




from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.

from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """


    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        

        data = serializer.save()
        print(data)
        data= serializer.data
        print(data)
        return Response(data)


















































































def testing(request, *args, **kwargs):
    result = request.body
 
    data = {}
    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        data = {"error" : "invalid json data"}

    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type  # Correct content_type attribute
    data["params"] = dict(request.GET)
    
    return JsonResponse(data)


def testing2(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}

    if instance:


        a = """data['id']  = instance.id
        data['title']= instance.title
        data["content"] =  instance.content
        data['price'] =  instance.price"""

    # model instance (model data)
    # turn it into a python dict
    # return JSON to my client 

        data = model_to_dict(instance, fields=["id", "title"])

    return JsonResponse(data)







@api_view(["GET"])
def testing3(request, *args, **kwargs):
    """DRF API View"""

    
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(instance, fields={"id", "title", "price", 'sale_price'})
        data = ProductSerializer(instance).data

    return Response(data)

