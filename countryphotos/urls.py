from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('countryimage/<int:pk>', views.countryimage, name = 'countryimage'),
    path('addcountries',  views.addcountries, name = 'addcountries'),
    
]
