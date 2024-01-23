from django.shortcuts import render

def home(request):
    # shyam shrama
    return render(request, 'index.html')