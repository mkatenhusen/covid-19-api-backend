from django.contrib import admin

from covid19_backend.daily_data.models import DailyCase, GenderAgeRelation, Age


@admin.register(DailyCase)
class DailyCaseAdmin(admin.ModelAdmin):
    list_display = ("date_day", "infected_total", "deaths_total", "healed_total", "get_county")

    def get_county(self, obj: DailyCase):
        return obj.county.name


@admin.register(GenderAgeRelation)
class GenderAgeRelationAdmin(admin.ModelAdmin):
    list_display = ("date_day", "gender_count", "age_group", "get_county")

    def gender_count(self, obj: GenderAgeRelation):
        return obj.gender.name

    def age_group(self, obj: GenderAgeRelation):
        return obj.age.age_string

    def get_county(self, obj: GenderAgeRelation):
        return obj.county.name


@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):
    list_display = ("min", "max",)

