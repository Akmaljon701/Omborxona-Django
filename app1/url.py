from django.urls import path
from .views import *

urlpatterns = [

    path('', BolimView.as_view(), name='bolimlar'),
    path('mahsulotlar/', ProductsView.as_view(), name='mahsulotlar'),
    path('mahsulot_del/<int:pk>/', ProductDelView.as_view(), name='mahsulot-del'),
    path('mahsulot_update/<int:pk>/', ProductUpdateView.as_view(), name='mahsulot-update'),

    path('clientlar/', ClientsView.as_view(), name='clientlar'),
    path('client_del/<int:pk>/', ClientDelView.as_view(), name='client-del'),
    path('client_update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),

]
