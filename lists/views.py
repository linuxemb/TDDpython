from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# home_page= None
# def home_page():
#     pass
# def home_page(request):
#     return HttpResponse()  # False is not true

# def home_page(request):
#     return HttpResponse('<html><title>To-Do lists</title></html>')

def home_page(request):
    return render(request, 'home.html')