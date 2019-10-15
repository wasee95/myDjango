from django.conf.urls import url
from django.urls import path
from first_app import views
urlpatterns = [
                url(r'^$',views.index1,name='index1'),
                url(r'^$',views.audio,name='audio')
]
