from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def mc720(request):
    return render(request, 'mc720.html')


def mc750(request):
    return render(request, 'mc750.html')

def mc765(request):
    return render(request, 'mc765.html')
