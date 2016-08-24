from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

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


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
