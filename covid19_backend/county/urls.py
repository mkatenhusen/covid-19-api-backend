from rest_framework_nested import routers

from covid19_backend.county.views import CountyView


county_router = routers.DefaultRouter()
county_router.register(r'county', CountyView, basename='county')
