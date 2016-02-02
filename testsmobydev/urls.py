from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^', include('data.urls')),
]

urlpatterns += staticfiles_urlpatterns()
