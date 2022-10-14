from django.urls import path, include

from . import views


urlpatterns = [
    path('add_message/', views.add_message),
    path('auth/', include('rest_framework.urls')),
]