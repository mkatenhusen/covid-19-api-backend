from django.db import models
from django.utils.translation import ugettext_lazy as _


class State(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True, allow_unicode=True)


class County(models.Model):
    name = models.CharField(max_length=90, unique=True)
    slug = models.SlugField(max_length=90, unique=True, allow_unicode=True)
    ags = models.IntegerField(unique=True, help_text=_("Amtlicher Gemeindeschlüssel"))

    alternative_name = models.CharField(max_length=90, blank=True, null=True, help_text=_("Kurzbezeichnung"))
    description = models.CharField(max_length=200, blank=True, null=True,
                                   help_text=_("Typ der Gemeinde, bspw. kreisfreie Stadt"))

    population = models.BigIntegerField()
    population_density = models.BigIntegerField(blank=True, null=True)

    state = models.ForeignKey(to=State, on_delete=models.CASCADE)
