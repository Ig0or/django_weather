from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('reset', reset, name='reset')
]