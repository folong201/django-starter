 
from django.urls import path 
from . import  views

urlpatterns = [
    path("",views.index,name="home"),
    path('news/',views.news,name='news'),
    path("contact/",views.contact,name='contact'),
    path("product/",views.product,name='product'), 
]