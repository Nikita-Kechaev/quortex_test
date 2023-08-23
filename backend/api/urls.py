from django.urls import include, path
from rest_framework import routers

from .views import SingerViewSet

app_name = 'api'


router_v1 = routers.DefaultRouter()
router_v1.register("singers", SingerViewSet, basename="singers")


urlpatterns = [
    path("", include(router_v1.urls)),
]
