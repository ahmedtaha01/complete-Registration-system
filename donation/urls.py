from django.urls import path 

from .views import create


urlpatterns = [

    path('<int:projectid>/create',create)
] 