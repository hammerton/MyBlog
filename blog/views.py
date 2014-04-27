from django.shortcuts import render
from blog.models import BlogPosts

# Create your views here.
def home(request):
    return render(request, 'index.html', {"hello": "world"})