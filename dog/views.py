from django.shortcuts import render

# Create your views here.
def dogs(request):
    return render(request, 'dogs.html')

def Dog(request):
    return render(request, 'Dog.html')