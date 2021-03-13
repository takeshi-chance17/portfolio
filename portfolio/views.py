from django.shortcuts import render

def index(request):
    # return render(request, 'hello.html', {})
    return render(request, 'index.html', {})
