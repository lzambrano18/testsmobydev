from rest_framework import routers

from django.conf.urls import include, url

from .api import CauseViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cause', CauseViewSet, 'Cause')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
