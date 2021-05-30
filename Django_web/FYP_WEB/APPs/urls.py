from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



"""When ever someone calls from home, i.e. (''),
it leads to home
#views.home refers to the home function in views.py"""

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('home/', views.home, name='home'),

    path('data_set', views.data_set, name='data_set'),
    path('show_times/', views.show_times, name='show_times'),
    path('camera', views.camera, name='camera'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)