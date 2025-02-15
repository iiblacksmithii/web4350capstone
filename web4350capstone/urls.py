from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # Add this line

def homepage(request):
    return HttpResponse("<h1>Welcome to Web4350Capstone Project!2</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage)  # Add homepage route
]