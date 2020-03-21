from rest_framework import serializers

from covid19_backend.daily_data.models import GenderAgeRelation, DailyCase, Age, Gender


class DailyCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCase
        fields = ("infected_total", "deaths_total", "date_day")


class GenderAgeSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="gender.name", read_only=True)
    age_min = serializers.IntegerField(source="age.min", read_only=True)
    age_max = serializers.IntegerField(source="age.max", read_only=True)

    class Meta:
        model = GenderAgeRelation
        fields = ["count", "gender", "age_min", "age_max",]


class AgeSerializer(serializers.ModelSerializer):
    count = serializers.RelatedField(source="genderagerelation_set.count", read_only=True)

    class Meta:
        model = Age
        fields = ["count", "min", "max", "age_string"]


class GenderSerializer(serializers.ModelSerializer):
    count = serializers.RelatedField(source="genderagerelation.count", read_only=True)

    class Meta:
        model = Gender
        fields = ["count", "name"]
