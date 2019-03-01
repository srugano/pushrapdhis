from . import models
from . import serializers
from rest_framework import viewsets, permissions


class SiteMappingViewSet(viewsets.ModelViewSet):
    """ViewSet for the SiteMapping class"""

    queryset = models.SiteMapping.objects.all()
    serializer_class = serializers.SiteMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
