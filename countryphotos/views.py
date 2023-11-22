from django.shortcuts import render



def home(request):
    return render(request, 'countryphotos/home.html')

def countryimage(request, pk):
    return render(request, 'countryphotos/countryimage.html')

def addcountries(request):
    return render(request, 'countryphotos/addcountries.html')





# Create your views here.
