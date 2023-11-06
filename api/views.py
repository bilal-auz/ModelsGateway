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
    if(not request.body):  return HttpResponse("No Body")
    body = json.loads(request.body)

    if('context' in body and 'question' in body):
        context = body['context']
        question = body['question']
        data = bert_large_service(context, question)
    else:
        data = "Empty Body"

    return HttpResponse(data)


