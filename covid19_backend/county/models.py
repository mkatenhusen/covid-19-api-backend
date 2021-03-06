from django.db import models
from django.utils.translation import ugettext_lazy as _


class State(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(max_length=90, unique=True)
    ags = models.CharField(unique=True, help_text=_("Amtlicher Gemeindeschlüssel"), max_length=10)

    gen = models.CharField(max_length=90, blank=True, null=True, help_text=_("Kurzbezeichnung"))
    bez = models.CharField(max_length=200, blank=True, null=True,
                           help_text=_("Typ der Gemeinde, bspw. kreisfreie Stadt"))

    population = models.BigIntegerField(blank=True, null=True)
    population_male = models.BigIntegerField(blank=True, null=True)
    population_female = models.BigIntegerField(blank=True, null=True)
    population_density_km = models.FloatField(blank=True, null=True)

    state = models.ForeignKey(to=State, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("name", "state", "ags")

    def __str__(self):
        return self.name
