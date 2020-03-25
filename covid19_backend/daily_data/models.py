from django.db import models

from covid19_backend.county.models import County


class DailyCase(models.Model):
    infected_total = models.IntegerField()
    deaths_total = models.IntegerField(null=True, blank=True)
    healed_total = models.IntegerField(null=True, blank=True)
    immune_total = models.IntegerField(null=True, blank=True)
    intensive_total = models.IntegerField(null=True, blank=True)
    quarantine_total = models.IntegerField(null=True, blank=True)
    infected_per_100k = models.FloatField(null=True, blank=True)
    death_rate = models.FloatField(null=True, blank=True)

    date_day = models.DateField()

    last_updated = models.DateTimeField()

    county = models.ForeignKey(to=County, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("date_day", "county")


class Age(models.Model):
    name = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.name


class GenderAgeRelation(models.Model):
    county = models.ForeignKey(to=County, on_delete=models.CASCADE)
    date_day = models.DateField()

    infected_total = models.IntegerField(null=True, blank=True)
    deaths_total = models.IntegerField(null=True, blank=True)

    age = models.ForeignKey(to=Age, on_delete=models.CASCADE)
    gender = models.ForeignKey(to=Gender, on_delete=models.CASCADE)

    last_updated = models.DateTimeField()

    class Meta:
        unique_together = ("county", "date_day", "age", "gender")
