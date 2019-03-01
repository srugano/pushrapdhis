from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r"sitemapping", api.SiteMappingViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path("api/v1/", include(router.urls)),
)

urlpatterns += (
    # urls for SiteMapping
    path(
        "rapdhis/sitemapping/",
        views.SiteMappingListView.as_view(),
        name="rapdhis_sitemapping_list",
    ),
    path(
        "rapdhis/sitemapping/create/",
        views.SiteMappingCreateView.as_view(),
        name="rapdhis_sitemapping_create",
    ),
    path(
        "rapdhis/sitemapping/detail/<int:pk>/",
        views.SiteMappingDetailView.as_view(),
        name="rapdhis_sitemapping_detail",
    ),
    path(
        "rapdhis/sitemapping/update/<int:pk>/",
        views.SiteMappingUpdateView.as_view(),
        name="rapdhis_sitemapping_update",
    ),
    path("rapdhis/process_request/", views.process_request, name="process_request"),
)
