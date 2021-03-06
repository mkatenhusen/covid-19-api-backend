from django.contrib import admin

from covid19_backend.daily_data.models import DailyCase, GenderAgeRelation, Age, Gender


@admin.register(DailyCase)
class DailyCaseAdmin(admin.ModelAdmin):
    list_display = ("date_day", "infected_total", "deaths_total", "healed_total", "get_county")

    def get_county(self, obj: DailyCase):
        return obj.county.name


@admin.register(GenderAgeRelation)
class GenderAgeRelationAdmin(admin.ModelAdmin):
    list_display = ("infected_total", "date_day", "gender_name", "age_group", "get_county")

    def gender_name(self, obj: GenderAgeRelation):
        return obj.gender.name

    def age_group(self, obj: GenderAgeRelation):
        return obj.age.name

    def get_county(self, obj: GenderAgeRelation):
        return obj.county.name


@admin.register(Age)
class AgeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ("name",)

