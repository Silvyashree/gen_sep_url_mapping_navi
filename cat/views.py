from django.shortcuts import render

# Create your views here.
def Caat(request):
    return render(request, 'Caat.html')

def kitten(request):
    return render(request, 'kitten.html')