from django.contrib import admin
admin.autodiscover()

from django.conf.urls import *

# This two if you want to enable the Django Admin: (recommended)
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # ... your url patterns
]
