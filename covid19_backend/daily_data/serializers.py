from rest_framework import serializers

from covid19_backend.county.models import County
from covid19_backend.daily_data.models import GenderAgeRelation, DailyCase, Age, Gender


class DailyCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyCase
        fields = ("infected_total", "deaths_total", "intensive_total", "immune_total", "date_day", "quarantine_total",
                  "infected_per_100k", "death_rate", "last_updated")

    def create(self, validated_data):
        county = County.objects.get(slug=self.context["county__ags"])
        try:
            daily_cases: DailyCase = \
                DailyCase.objects.get(county=county,
                                      date_day=validated_data.get("date_day"))
            if daily_cases.last_updated > validated_data.get("last_updated"):
                raise serializers.ValidationError({"message": "Newer dataset already saved"})
            else:
                daily_cases.infected_total = validated_data.get("infected_total")
                daily_cases.deaths_total = validated_data.get("deaths_total")
                daily_cases.healed_total = validated_data.get("healed_total")
                daily_cases.intensive_total = validated_data.get("intensive_total")
                daily_cases.immune_total = validated_data.get("immune_total")
                daily_cases.quarantine_total = validated_data.get("quarantine_total")
                daily_cases.infected_per_100k = validated_data.get("infected_per_100k")
                daily_cases.death_rate = validated_data.get("death_rate")
                daily_cases.last_updated = validated_data.get("last_updated")
                daily_cases.save()
                return daily_cases
        except DailyCase.DoesNotExist:
            return DailyCase.objects.create(last_updated=validated_data.get("last_updated"),
                                            date_day=validated_data.get("date_day"),
                                            county=county,
                                            infected_total=validated_data.get("infected_total"),
                                            healed_total=validated_data.get("healed_total"),
                                            immune_total=validated_data.get("immune_total"),
                                            deaths_total=validated_data.get("deaths_total"),
                                            intensive_total=validated_data.get("intensive_total"),
                                            quarantine_total=validated_data.get("quarantine_total"),
                                            infected_per_100k=validated_data.get("infected_per_100k"),
                                            death_rate=validated_data.get("death_rate"),
                                            )


class GenderAgeSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="gender.name")
    age_group = serializers.CharField(source="age.name")

    class Meta:
        model = GenderAgeRelation
        fields = ["count", "gender", "age_group", "date_day", "last_updated"]

    def create(self, validated_data):
        county = County.objects.get(ags=self.context["county__ags"])
        try:
            latest_gender_age_relation: GenderAgeRelation = \
                GenderAgeRelation.objects.get(gender__name=validated_data.get("gender").get("name"),
                                              age__name=validated_data.get("age").get("name"),
                                              date_day=validated_data.get("date_day"),
                                              county=county)
            if latest_gender_age_relation.last_updated > validated_data.get("last_updated"):
                raise serializers.ValidationError({"message": "Newer dataset already saved"})
            else:
                latest_gender_age_relation.count = validated_data.get("count")
                latest_gender_age_relation.last_updated = validated_data.get("last_updated")
                latest_gender_age_relation.save()
                return latest_gender_age_relation
        except GenderAgeRelation.DoesNotExist:
            age = Age.objects.get(name=validated_data.get("age").get("name"))
            gender = Gender.objects.get(name=validated_data.get("gender").get("name"))
            return GenderAgeRelation.objects.create(age=age,
                                                    gender=gender,
                                                    county=county,
                                                    count=validated_data.get("count"),
                                                    last_updated=validated_data.get("last_updated"),
                                                    date_day=validated_data.get("date_day"))


class AgeSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source="genderagerelation_set.first.count", read_only=True)
    date_day = serializers.DateField(source="genderagerelation_set.first.date_day", read_only=True)
    count = serializers.SerializerMethodField(method_name="get_count")

    class Meta:
        model = Age
        fields = ["count", "min", "max", "age_string", "date_day",]

    def get_count(self, obj: Age):
        print(obj.genderagerelation_set.filter(age=self, ))
        print(self)
        return obj.genderagerelation_set.all()


class GenderSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source="genderagerelation_set.first.count", read_only=True)

    class Meta:
        model = Gender
        fields = ["count", "name"]
