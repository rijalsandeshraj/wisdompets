from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(\d+)/', views.pet_detail, name='pet_detail'),
]
