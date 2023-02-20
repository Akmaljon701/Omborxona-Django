from django.urls import path
from .views import *

urlpatterns = [

    path('', BolimView.as_view()),

]
