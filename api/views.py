import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from api.services import bert_large_service, bert_large_service_huggingFace_API, falcon_service

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
    if(not request.query_params['model_name']): return HttpResponse("No Model")

    context = request.query_params['context']
    question = request.query_params['question']
    model_name = request.query_params['model_name']
    
    # Run Locally
    data = bert_large_service(context, question, model_name)

    return HttpResponse(data)

@api_view(['GET'])
def falcon(request):
    if(not request.query_params['question']): return HttpResponse("No Question")
    if(not request.query_params['model_name']): return HttpResponse("No Model")

    question = request.query_params['question']
    model_name = request.query_params['model_name']
    max_length = 200

    data = falcon_service(question, model_name, max_length)

    return HttpResponse(data)


@api_view(['GET'])
def bert_large_HuggingFaceAPI(request):
    if(not request.query_params['context']): return HttpResponse("No Context")
    if(not request.query_params['question']): return HttpResponse("No Question")
    if(not request.query_params['model_name']): return HttpResponse("No Model")

    context = request.query_params['context']
    question = request.query_params['question']
    model_name = request.query_params['model_name']

    # Using Hugging Face API
    data = bert_large_service_huggingFace_API(context, question, model_name)

    return HttpResponse(data)
