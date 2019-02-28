from django.contrib import admin
from django import forms
from .models import SiteMapping

class SiteMappingAdminForm(forms.ModelForm):

    class Meta:
        model = SiteMapping
        fields = '__all__'


class SiteMappingAdmin(admin.ModelAdmin):
    form = SiteMappingAdminForm
    list_display = ['dhisorgname', 'dhisorguid', 'dhisorgparent', 'rproorgname', 'rproorgid', 'rproorgparent', 'commune']
    readonly_fields = ['dhisorgname', 'dhisorguid', 'dhisorgparent', 'rproorgname', 'rproorgid', 'rproorgparent', 'commune']

admin.site.register(SiteMapping, SiteMappingAdmin)


