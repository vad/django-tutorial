import csv

from django.core.management.base import BaseCommand, CommandError
from veicoli.models import Veicolo


def in_regola_to_bool(c):
    if c == 'S':
        return True
    elif c == 'N':
        return False
    else:
        return None


def blankable_str_to_int(s):
    if s:
        return int(s)
    return None


class Command(BaseCommand):
    help = 'Carica parco circolante CSV'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        fn = options['path']
        with open(fn) as f:
            reader = csv.DictReader(f)
            for datum in reader:
                datum['id_veicolo'] = datum.pop('id')
                datum['revisione_in_regola'] = in_regola_to_bool(datum.get('revisione_in_regola'))
                datum['assicurazione_in_regola'] = in_regola_to_bool(datum.get('assicurazione_in_regola'))
                datum['eta_intestatario'] = blankable_str_to_int(datum.get('eta_intestatario'))
                datum['emissioni_co2'] = blankable_str_to_int(datum.get('emissioni_co2'))
                print(datum)
                v = Veicolo(**datum)
                v.save()
