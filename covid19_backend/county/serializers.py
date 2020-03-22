from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from covid19_backend.county.models import State, County


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ("name", "slug")


class CountySerializer(serializers.ModelSerializer):
    state = serializers.CharField(source="state.name", read_only=False)

    class Meta:
        model = County
        fields = ("name", "slug", "ags", "state", "alternative_name", "description", "population", "population_density")

    def create(self, validated_data):
        try:
            validated_data["state"] = State.objects.get(name=validated_data.get("state").get("name"))
            return super().create(validated_data)
        except State.DoesNotExist:
            raise serializers.ValidationError({"message": _("The state object does not exist")})
