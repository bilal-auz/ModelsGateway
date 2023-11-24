from django.urls import path

from .views import falcon, index, bert_large, bert_large_HuggingFaceAPI


urlpatterns = [
    path('', index),
    path('/model/bert-large', bert_large),
    path('/model/falcon', falcon),
    path('/model/huggingface/bert-large', bert_large_HuggingFaceAPI),
]