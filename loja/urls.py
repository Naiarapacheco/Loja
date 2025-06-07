from django.contrib import admin
from django.urls import path

from base.views import base

urlpatterns = [
    path('', base, name="base"),
    path('admin/', admin.site.urls),
]
