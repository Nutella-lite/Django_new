from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('django_guide', views.django_guide, name='guide'),
    path('parsing_tools', views.parsing_tools, name='tools'),
    path('faq', views.faq, name='faq'),
]