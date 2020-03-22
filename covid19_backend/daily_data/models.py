from django.db import models

from covid19_backend.county.models import County


class DailyCase(models.Model):
    infected_total = models.IntegerField()
    deaths_total = models.IntegerField()
    healed_total = models.IntegerField(null=True, blank=True)
    immune_total = models.IntegerField(null=True, blank=True)
    intensive_total = models.IntegerField(null=True, blank=True)

    date_day = models.DateField()

    last_updated = models.DateTimeField()

    county = models.ForeignKey(to=County, on_delete=models.CASCADE)


class Age(models.Model):
    min = models.SmallIntegerField()
    max = models.SmallIntegerField()

    @property
    def age_string(self):
        return str(self.min) + "-" + str(self.max)

    @age_string.setter
    def age_string(self, value):
        split = value.split("-")
        self.min = split[0]
        self.max = split[1]


class Gender(models.Model):
    name = models.CharField(max_length=6, unique=True)


class GenderAgeRelation(models.Model):
    county = models.ForeignKey(to=County, on_delete=models.CASCADE)
    date_day = models.DateField()

    count = models.IntegerField()

    age = models.ForeignKey(to=Age, on_delete=models.CASCADE)
    gender = models.ForeignKey(to=Gender, on_delete=models.CASCADE)

    last_updated = models.DateTimeField()

    class Meta:
        unique_together = ("county", "date_day", "age", "gender")
