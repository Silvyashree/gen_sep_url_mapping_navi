from cat.views import *
from django.urls import path

app_name= 'Caat'

urlpatterns = [
    path('Caat/', Caat , name='Caat'),
    path('kitten/',kitten,name='kitten'),
]
