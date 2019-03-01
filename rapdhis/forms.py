from django import forms
from .models import SiteMapping


class SiteMappingForm(forms.ModelForm):
    class Meta:
        model = SiteMapping
        fields = [
            "dhisorgname",
            "dhisorgparent",
            "rproorgname",
            "rproorgparent",
            "commune",
        ]
