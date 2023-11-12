import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from api.services import bert_large_service

@api_view(['GET'])
def index(request):
    html = f'''
    <html>
        <body>
            <h1>API is Working</h1>
        </body>
    </html>
    '''
    return HttpResponse(html)

@api_view(['GET'])
def bert_large(request):
    if(not request.query_params['context']): return HttpResponse("No Context")
    if(not request.query_params['question']): return HttpResponse("No Question")

    context = request.query_params['context']
    question = request.query_params['question']
    
    data = bert_large_service(context, question)

    return HttpResponse(data)


