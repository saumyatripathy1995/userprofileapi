from django.conf.urls import url
from django.contrib import admin
from.import views
urlpatterns=[
    url(r'^$',view=views.login,name="login"),
    url(r'^profiledisplay',view=views.profiledisplay,name="profilediplay"),
    url(r'^insertion',view=views.insert,name="insert"),
    url(r'^update',view=views.update,name="update")

]