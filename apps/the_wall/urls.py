from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login, name='thewall-login'),
    url(r'^register/$', views.register, name='thewall-register'),
    url(r'^dashboard/$', views.dashboard, name='thewall-dashboard'),
    # url(r'^login/$', views.login, name='thewall-login'),


]
