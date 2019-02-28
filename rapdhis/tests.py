import unittest
from django.urls import reverse
from django.test import Client
from .models import SiteMapping
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_sitemapping(**kwargs):
    defaults = {}
    defaults["dhisorgname"] = "dhisorgname"
    defaults["dhisorguid"] = "dhisorguid"
    defaults["dhisorgparent"] = "dhisorgparent"
    defaults["rproorgname"] = "rproorgname"
    defaults["rproorgid"] = "rproorgid"
    defaults["rproorgparent"] = "rproorgparent"
    defaults["commune"] = "commune"
    defaults.update(**kwargs)
    return SiteMapping.objects.create(**defaults)


class SiteMappingViewTest(unittest.TestCase):
    '''
    Tests for SiteMapping
    '''
    def setUp(self):
        self.client = Client()

    def test_list_sitemapping(self):
        url = reverse('rapdhis_sitemapping_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sitemapping(self):
        url = reverse('rapdhis_sitemapping_create')
        data = {
            "dhisorgname": "dhisorgname",
            "dhisorguid": "dhisorguid",
            "dhisorgparent": "dhisorgparent",
            "rproorgname": "rproorgname",
            "rproorgid": "rproorgid",
            "rproorgparent": "rproorgparent",
            "commune": "commune",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sitemapping(self):
        sitemapping = create_sitemapping()
        url = reverse('rapdhis_sitemapping_detail', args=[sitemapping.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sitemapping(self):
        sitemapping = create_sitemapping()
        data = {
            "dhisorgname": "dhisorgname",
            "dhisorguid": "dhisorguid",
            "dhisorgparent": "dhisorgparent",
            "rproorgname": "rproorgname",
            "rproorgid": "rproorgid",
            "rproorgparent": "rproorgparent",
            "commune": "commune",
        }
        url = reverse('rapdhis_sitemapping_update', args=[sitemapping.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


