from django.conf.urls import url
from . import views

# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^users$', views.register),
#     url(r'^login$', views.login),
#
# ]

urlpatterns = [
 url(r'^$', views.Register.as_view(), name='users-register'),
 url(r'^login/$', views.Login.as_view(), name='users-login'),
 url(r'^logout/$', views.Logout.as_view(), name='users-logout'),
]
