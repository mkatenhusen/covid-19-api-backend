from django.contrib import admin

from covid19_backend.county.models import State, County


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ("name", "ags", "get_state")

    def get_state(self, obj: County):
        return obj.state.name
