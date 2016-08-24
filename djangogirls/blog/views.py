from django.shortcuts import render

#where the logic of the application
def post_list(request):
    """function that takes request and returns a function render
    that will render the template blog/post_list.html 
    """
    return render(request, 'blog/post_list.html', {})
