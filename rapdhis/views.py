from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import SiteMapping
from .forms import SiteMappingForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from dhis2 import Dhis
from django.conf import settings


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


@csrf_exempt
def process_request(request):
    """This function receives requests sent by RapidPro.
    This function send json data to RapidPro as a response."""
    # We will put all data sent by RapidPro in this variable
    api = Dhis(settings.DHIS_URI, settings.DHIS_USERNAME, settings.DHIS_PASSWORD)

    # Let's put all the incoming data in the dictionary 'incoming_data'
    incoming_data = json.loads(request.body.decode("utf-8"))["input"]["text"].split()
    d = {}

    data = {
        "dataSet": "pBOMPrpg1QX",
        "completeDate": "2019-02-03",
        "period": int(incoming_data[0]),
        "orgUnit": "DiszpKrYNg8",
        "dataValues": [
            {"dataElement": "f7n9E0hX8qk", "value": int(incoming_data[1])},
            {"dataElement": "Ix2HsbDMLea", "value": int(incoming_data[2])},
            {"dataElement": "eY5ehpbEsB7", "value": int(incoming_data[3])},
        ],
    }

    r = api.post("dataValueSets", json=data)
    d["Ok"] = True
    d["message"] = "Rapport bien recu. Vous pouvez voir les valeurs dans la province Bo, district Badjia, le centre de sante Ngelehun CHC pour l indicateur Mortality < 5 yrs, les valeurs Cholera, Dysentery, Malaria qui ont change ici http://dhis.uniceburundi.org"
    return JsonResponse(d, safe=False)
