from django.views import generic
from django.http import HttpResponse

def homePage(request):
    return HttpResponse("<h1>Welcome</h1>") 