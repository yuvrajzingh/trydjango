from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs,):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    
    my_context = {
        "title": "an about page",
        "my_text": "This is about us.",
        "my_number": 123,
        "my_list": [124, 634, 632],
    }
    
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})