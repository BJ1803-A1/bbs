from django.conf.urls import url, include

from App import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^create_card/',views.create_card,name='creade_card'),
]