from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninja/$', views.allninjas),
    url(r'^ninja/(?P<ninja_color>\w+)/$', views.showninja),
]
