from django.contrib import admin
from django.urls import path, include
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bolim/', include('app1.url')),
    path('stats/', include('app2.url')),

    path('', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
