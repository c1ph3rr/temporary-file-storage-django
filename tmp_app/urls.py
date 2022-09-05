from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dl/<file_id>/<file_name>', views.redirect, name='redirect')
]
