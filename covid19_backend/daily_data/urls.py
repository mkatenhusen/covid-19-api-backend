from rest_framework_nested import routers

from covid19_backend.county.urls import county_router
from covid19_backend.daily_data.views import DailyCasesView, GenderAgeView, AgeView, GenderView

county_data_router = routers.NestedDefaultRouter(county_router, r'county', lookup='county_')
county_data_router.register(r'cases', DailyCasesView, basename='cases')
county_data_router.register(r'gender_age', GenderAgeView, basename='gender_age')
county_data_router.register(r'age', AgeView, basename='age')
county_data_router.register(r'gender', GenderView, basename='gender')
