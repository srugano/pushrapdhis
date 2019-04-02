from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import SiteMapping
from .forms import SiteMappingForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from dhis2 import Dhis
from django.conf import settings
import datetime 

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
        "completeDate": datetime.datetime.today().strftime('%Y-%m-%d'),
        "period": int(incoming_data[0]),
        "orgUnit": "DiszpKrYNg8",
        "dataValues": [
            {"dataElement":"hM4ya5T2AqX", "value": int(incoming_data[6])},
            {"dataElement":"Yy9NtNfwYZJ", "value": int(incoming_data[11])},
            {"dataElement":"Vp12ncSU1Av", "value": int(incoming_data[10])},
            {"dataElement":"NpJtsQkMTm3", "value": int(incoming_data[14])},
            {"dataElement":"jVDAvs6kIAP", "value": int(incoming_data[4])},
            {"dataElement":"FTRrcoaog83", "value": int(incoming_data[13])},
            {"dataElement":"MSZuQ1mTsia", "value": int(incoming_data[12])},
            {"dataElement":"lXolhoWewYH", "value": int(incoming_data[7])},
            {"dataElement":"USBq0VHSkZq", "value": int(incoming_data[8])},
            {"dataElement":"eY5ehpbEsB7", "value": int(incoming_data[5])},
            {"dataElement":"LjNlMTl9Nq9", "value": int(incoming_data[3])},
            {"dataElement":"f7n9E0hX8qk", "value": int(incoming_data[1])},
            {"dataElement":"r6nrJANOqMw", "value": int(incoming_data[2])},
            {"dataElement":"Ix2HsbDMLea", "value": int(incoming_data[9])}
        ],
    }

    r = api.post("dataValueSets", json=data)
    d["Ok"] = True
    d["message"] = "Rapport bien recu. Vous pouvez voir les valeurs dans la province Bo, district Badjia, le centre de sante Ngelehun CHC pour l indicateur Mortality < 5 yrs, les valeurs Cholera, Dysentery, Malaria qui ont change ici http://dhis.uniceburundi.org"
    return JsonResponse(d, safe=False)
