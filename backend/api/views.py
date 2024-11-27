from django.shortcuts import render
import json

# Create your views here.

from django.http import JsonResponse

def api_home(request, *args, **kwargs):
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

