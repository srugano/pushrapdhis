from . import models

from rest_framework import serializers


class SiteMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SiteMapping
        fields = (
            'pk', 
            'dhisorgname', 
            'dhisorguid', 
            'dhisorgparent', 
            'rproorgname', 
            'rproorgid', 
            'rproorgparent', 
            'commune', 
        )


