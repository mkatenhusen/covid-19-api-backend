"""covid19_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi, views
from rest_framework import permissions

from covid19_backend.county.urls import county_router
from covid19_backend.daily_data.urls import county_data_router

urlpatterns = [
    path('api/v0.1/', include(county_router.urls)),
    path('api/v0.1/', include(county_data_router.urls)),
    path('admin/', admin.site.urls),
]

schema_view = views.get_schema_view(
   openapi.Info(
      title="Covid-19 Landkreis API",
      default_version='v0.1',
      description="Daten zu Infizierten und mehr des Corona-Virus auf Landkreisebene",
      license=openapi.License(name="Daten vom RKI"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]