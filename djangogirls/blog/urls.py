#imports django function url and views from the blog app
from django.conf.urls import url
from . import views

urlpatterns = [
#assigns a view called post_list to ^$ url.
#th rege matches a ^beginning followed by an $end
#name="post_list" this is the name of the url used to identify the view
    url(r'^$', views.post_list, name='post_list'),
]
