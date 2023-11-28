from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return  render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return  render(request, "contact.html", {})
    
def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number" : 123,
        "my_list": [1,4343, 123123, "about"]
    }
    # for item in [123,9129,100]:
    #     context['item1'] = item
    return  render(request, "about.html", {})

def social_view(*args, **kwargs):
    return  render("social.html", {})

def index_view(request, *args, **kwargs):
    return  render(request,"index.html", {})
