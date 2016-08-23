
from django.contrib import admin
from .models import Post

#makes the model visible on the admin page
admin.site.register(Post)
