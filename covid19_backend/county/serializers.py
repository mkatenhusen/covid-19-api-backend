from rest_framework import serializers

from covid19_backend.county.models import State, County


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ("name", "slug")


class CountySerializer(serializers.ModelSerializer):
    state = serializers.CharField(source="state.name", read_only=True)

    class Meta:
        model = County
        fields = ("name", "slug", "ags", "state", "alternative_name", "description", "population", "population_density")
