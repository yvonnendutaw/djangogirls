from django.shortcuts import render
#the . means current directory
#used here as the views.py and models.py are in the same directory
from .models import Post
from django.utils import timezone

#where the logic of the application is
def post_list(request):
    """function that takes request and returns a function render
    that will render the template blog/post_list.html 
    """
    #queryset to order the blog posts by published date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #{} this is where we can store things the template will use 
    return render(request, 'blog/post_list.html', {'posts' : posts})

