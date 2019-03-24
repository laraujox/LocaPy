from django.shortcuts import render

# Create your views here.


def index(request):
    return render (request,'index.html')
def fotos(request):
    return render (request,'fotos.html')