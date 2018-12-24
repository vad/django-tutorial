from django.http import JsonResponse

from .models import Veicolo


def index(request):
    veicoli = Veicolo.objects.all()
    for filtername, value in request.GET:
        veicoli = veicoli.filter(**{filtername: value})

    out = []
    for veicolo in veicoli:
        out.append({
            'comune': veicolo.comune,
        }
    )

    return JsonResponse(out, safe=False)
