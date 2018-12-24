from django.db import models


class Veicolo(models.Model):
    id_veicolo = models.IntegerField()
    progressivo = models.IntegerField()
    tipo_veicolo = models.CharField(max_length=1)
    destinazione = models.CharField(max_length=200)
    uso = models.CharField(max_length=200)
    comune_residenza = models.CharField(max_length=200)
    provincia_residenza = models.CharField(max_length=200)
    regione_residenza = models.CharField(max_length=200)
    eta_intestatario = models.IntegerField(null=True, blank=True)
    sesso = models.CharField(max_length=200, null=True, blank=True)
    marca = models.CharField(max_length=200, null=True, blank=True)
    cilindrata = models.FloatField()
    alimentazione = models.CharField(max_length=200)
    kw = models.IntegerField()
    data_immatricolazione = models.CharField(max_length=200)
    classe_euro = models.IntegerField()
    emissioni_co2 = models.IntegerField(null=True, blank=True)
    massa_complessiva = models.IntegerField()
    revisione_in_regola = models.BooleanField(null=True)
    assicurazione_in_regola = models.BooleanField(null=True)

