from django.shortcuts import render
from blog.models import BlogPosts

# Create your views here.
def home(request):
    blogposts = BlogPosts.objects.all()[:10:-1]
    return render(request, 'index.html', {'blogposts': blogposts})