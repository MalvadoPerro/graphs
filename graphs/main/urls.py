from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('params', views.param, name='params'),
    path('visual', views.visual, name='visual')
]