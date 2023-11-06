from django.urls import path

from .views import index, bert_large


urlpatterns = [
    path('', index),
    path('/model/bert-large', bert_large)
]