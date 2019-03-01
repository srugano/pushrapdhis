from django.views.generic.base import TemplateView
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^rapdhis/", include("rapdhis.urls")),
    url(r"^$", TemplateView.as_view(template_name="landing.html"), name="home"),
]
