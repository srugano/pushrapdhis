from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import UUIDField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
import uuid


class Indicator(models.Model):
    displayName = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True, default=uuid.uuid4)


class OrganisationUnit(models.Model):
    displayName = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True, default=uuid.uuid4)


class DataElement(models.Model):
    displayName = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True, default=uuid.uuid4)


class DataSets(models.Model):
    displayName = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True, default=uuid.uuid4)


class SiteMapping(models.Model):

    # Fields
    dhisorgname = models.CharField(max_length=255)
    dhisorguid = models.UUIDField(default=uuid.uuid4)
    dhisorgparent = models.CharField(max_length=255)
    rproorgname = models.CharField(max_length=255)
    rproorgid = models.UUIDField(default=uuid.uuid4)
    rproorgparent = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)

    class Meta:
        ordering = ("-pk",)

    def __unicode__(self):
        return u"%s" % self.pk

    def get_absolute_url(self):
        return reverse("rapdhis_sitemapping_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("rapdhis_sitemapping_update", args=(self.pk,))
