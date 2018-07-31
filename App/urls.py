from django.conf.urls import url, include

from App import views

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^create_card/',views.create_card,name='creade_card'),
    url(r'^card_content/card_id=(\d+)/',views.card_content,name='card_content')
]