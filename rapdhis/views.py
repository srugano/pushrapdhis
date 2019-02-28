from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import SiteMapping
from .forms import SiteMappingForm


class SiteMappingListView(ListView):
    model = SiteMapping


class SiteMappingCreateView(CreateView):
    model = SiteMapping
    form_class = SiteMappingForm


class SiteMappingDetailView(DetailView):
    model = SiteMapping


class SiteMappingUpdateView(UpdateView):
    model = SiteMapping
    form_class = SiteMappingForm

