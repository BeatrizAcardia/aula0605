from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    print('Teste de Home')
    return render(request, 'home.html')