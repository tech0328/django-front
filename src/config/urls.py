"""Root URL Configuration for Startup Organizer Project"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from blog import urls as blog_urls
from blog.routers import urlpatterns as blog_api_urls
from organizer import urls as organizer_urls
from organizer.routers import (
    urlpatterns as organizer_api_urls,
)

from .views import RootApiView

root_api_url = [
    path("", RootApiView.as_view(), name="api-root")
]
api_urls = root_api_url + blog_api_urls + organizer_api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_urls)),
    path("blog/", include(blog_urls)),
    path("", include(organizer_urls)),
    path(
        "",
        TemplateView.as_view(template_name="root.html"),
        name="site_root",
    ),
]
